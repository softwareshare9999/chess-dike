package com.xqdk.chess.i18n

import android.content.Context
import com.xqdk.chess.R
import com.xqdk.chess.gamelogic.Board
import com.xqdk.chess.gamelogic.Move
import com.xqdk.chess.gamelogic.Piece
import com.xqdk.chess.gamelogic.Position
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.RuntimeEnvironment
import org.robolectric.annotation.Config

/**
 * 记号器（Move.ChsTokens）切换的语义契约：
 * 默认中文输出与历史逐字节一致；安装 [MoveNotation] 后，着法描述词随应用语言变化，
 * 而棋盘棋子字形（Piece.pieceNameMap）保持中文不动。
 */
@RunWith(RobolectricTestRunner::class)
@Config(sdk = [34])
class MoveNotationTest {

    private lateinit var app: Context

    @Before
    fun setUp() {
        app = RuntimeEnvironment.getApplication()
        MoveNotation.install()
    }

    @After
    fun tearDown() {
        // 还原默认中文记号，避免污染同 JVM 内的其它测试
        Move.setChsTokens(Move.ZH_TOKENS)
    }

    @Test
    fun `default tokens reproduce historical Chinese output`() {
        Move.setChsTokens(Move.ZH_TOKENS)
        assertEquals("车一进六", redChariot().getChsString())
        assertEquals("车4退1", blackChariot().getChsString())
    }

    @Test
    fun `vietnamese tokens localize notation words only`() {
        val move = redChariot()
        // 越南语：Xe (chariot) + 1 + tiến (advance) + 6
        assertEquals("Xe1tiến6", move.getChsString())
    }

    @Test
    fun `black move uses localized name with arabic numerals`() {
        assertEquals("Xe4thoái1", blackChariot().getChsString())
    }

    @Test
    fun `board glyphs stay chinese regardless of language`() {
        // 棋盘绘制依赖 pieceNameMap，属于字形不是文案——切语言不得改变
        assertEquals('车', Piece.pieceNameMap[Piece.WJU])
        assertEquals('将', Piece.pieceNameMap[Piece.BJIANG])
    }

    @Test
    fun `zh resources still render chinese notation`() {
        val zh = app.createConfigurationContext(
            android.content.res.Configuration(app.resources.configuration).apply {
                setLocale(java.util.Locale.SIMPLIFIED_CHINESE)
            }
        )
        // 资源侧中文词表仍在：直接校验资源值，避免依赖进程级 Locale 切换时序
        assertEquals("进", zh.getString(R.string.move_action_advance))
        assertEquals("退", zh.getString(R.string.move_action_retreat))
        assertEquals("车", zh.getString(R.string.move_piece_w_chariot))
        assertEquals("一", zh.getString(R.string.num_1))
    }

    @Test
    fun `default locale resources are vietnamese`() {
        assertEquals("tiến", app.getString(R.string.move_action_advance))
        assertEquals("thoái", app.getString(R.string.move_action_retreat))
        assertEquals("Xe", app.getString(R.string.move_piece_w_chariot))
        assertTrue(app.getString(R.string.app_name).isNotEmpty())
    }

    private fun redChariot(): Move {
        val board = Board()
        val move = Move(board)
        move.fromPosition = Position(8, 9)
        move.toPosition = Position(8, 3)
        move.board.setPieceByPosition(move.fromPosition, Piece.WJU)
        return move
    }

    private fun blackChariot(): Move {
        val board = Board()
        val move = Move(board)
        move.fromPosition = Position(3, 9)
        move.toPosition = Position(3, 8)
        move.board.setPieceByPosition(move.fromPosition, Piece.BJU)
        return move
    }
}

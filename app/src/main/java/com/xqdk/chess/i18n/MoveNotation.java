package com.xqdk.chess.i18n;

import com.xqdk.chess.R;
import com.xqdk.chess.gamelogic.Move;
import com.xqdk.chess.gamelogic.Piece;

/**
 * Localized move-notation tokens.
 *
 * <p>Board glyphs stay Chinese (pieces are drawn as 帅/将/车… on the board itself);
 * only the <em>notation words</em> — piece names in prose, 平/进/退, 前/后/中 and the
 * file numerals — follow the app language. Installed via {@link #install()}.
 */
public final class MoveNotation implements Move.ChsTokens {

    private MoveNotation() {}

    /** Install the resource-backed token set (call once after the app context exists). */
    public static void install() {
        Move.setChsTokens(new MoveNotation());
    }

    /** Resource id for a piece's notation name, or 0 when unknown. */
    private static int pieceNameRes(int piece) {
        switch (piece) {
            case Piece.WSHUAI: return R.string.move_piece_w_king;
            case Piece.WSHI:   return R.string.move_piece_w_advisor;
            case Piece.WXIANG: return R.string.move_piece_w_elephant;
            case Piece.WMA:    return R.string.move_piece_w_horse;
            case Piece.WJU:    return R.string.move_piece_w_chariot;
            case Piece.WPAO:   return R.string.move_piece_w_cannon;
            case Piece.WBING:  return R.string.move_piece_w_pawn;
            case Piece.BJIANG: return R.string.move_piece_b_king;
            case Piece.BSHI:   return R.string.move_piece_b_advisor;
            case Piece.BXIANG: return R.string.move_piece_b_elephant;
            case Piece.BMA:    return R.string.move_piece_b_horse;
            case Piece.BJU:    return R.string.move_piece_b_chariot;
            case Piece.BPAO:   return R.string.move_piece_b_cannon;
            case Piece.BZU:    return R.string.move_piece_b_pawn;
            default: return 0;
        }
    }

    /**
     * Char-returning legacy hook retained for callers that only need the first
     * character. Vietnamese piece names are multi-character (e.g. "Tượng"), so
     * {@link Move} concatenates the full name via {@link #pieceName(int)}.
     */
    @Override
    public String pieceName(int piece) {
        return pieceNameText(piece);
    }

    /** Full localized piece name (multi-char in Vietnamese). */
    public static String pieceNameText(int piece) {
        int id = pieceNameRes(piece);
        return id == 0 ? "" : Res.get(id);
    }

    @Override public String actionFlat()    { return Res.get(R.string.move_action_flat); }
    @Override public String actionAdvance() { return Res.get(R.string.move_action_advance); }
    @Override public String actionRetreat() { return Res.get(R.string.move_action_retreat); }
    @Override public String prefixFront()   { return Res.get(R.string.move_prefix_front); }
    @Override public String prefixBack()    { return Res.get(R.string.move_prefix_back); }
    @Override public String prefixMid()     { return Res.get(R.string.move_prefix_mid); }
    @Override public String unknown()       { return Res.get(R.string.move_unknown); }

    /** Black files/ranks stay Arabic in every language (UCCI convention). */
    @Override public String blackNumeral(int n) { return String.valueOf(n); }

    /** Red files/ranks: Chinese numerals in zh, Arabic in vi. */
    @Override public String redNumeral(int n) {
        switch (n) {
            case 1: return Res.get(R.string.num_1);
            case 2: return Res.get(R.string.num_2);
            case 3: return Res.get(R.string.num_3);
            case 4: return Res.get(R.string.num_4);
            case 5: return Res.get(R.string.num_5);
            case 6: return Res.get(R.string.num_6);
            case 7: return Res.get(R.string.num_7);
            case 8: return Res.get(R.string.num_8);
            case 9: return Res.get(R.string.num_9);
            default: return String.valueOf(n);
        }
    }
}

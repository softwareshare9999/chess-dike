package com.xqdk.chess.i18n;

import com.xqdk.chess.R;
import com.xqdk.chess.gamelogic.Piece;

/**
 * Localized move-notation tokens. Board piece glyphs stay Chinese via {@link Piece#pieceNameMap}.
 */
public final class MoveNotation {
    private MoveNotation() {}

    public static String pieceName(int piece) {
        int id;
        switch (piece) {
            case Piece.WSHUAI: id = R.string.move_piece_w_king; break;
            case Piece.WSHI: id = R.string.move_piece_w_advisor; break;
            case Piece.WXIANG: id = R.string.move_piece_w_elephant; break;
            case Piece.WMA: id = R.string.move_piece_w_horse; break;
            case Piece.WJU: id = R.string.move_piece_w_chariot; break;
            case Piece.WPAO: id = R.string.move_piece_w_cannon; break;
            case Piece.WBING: id = R.string.move_piece_w_pawn; break;
            case Piece.BJIANG: id = R.string.move_piece_b_king; break;
            case Piece.BSHI: id = R.string.move_piece_b_advisor; break;
            case Piece.BXIANG: id = R.string.move_piece_b_elephant; break;
            case Piece.BMA: id = R.string.move_piece_b_horse; break;
            case Piece.BJU: id = R.string.move_piece_b_chariot; break;
            case Piece.BPAO: id = R.string.move_piece_b_cannon; break;
            case Piece.BZU: id = R.string.move_piece_b_pawn; break;
            default: return "";
        }
        return Res.get(id);
    }

    public static String actionFlat() { return Res.get(R.string.move_action_flat); }
    public static String actionAdvance() { return Res.get(R.string.move_action_advance); }
    public static String actionRetreat() { return Res.get(R.string.move_action_retreat); }
    public static String prefixFront() { return Res.get(R.string.move_prefix_front); }
    public static String prefixBack() { return Res.get(R.string.move_prefix_back); }
    public static String prefixMid() { return Res.get(R.string.move_prefix_mid); }
    public static String unknown() { return Res.get(R.string.move_unknown); }

    /** Red-side file/rank numerals (Chinese digits in zh, Arabic in vi). */
    public static String redNumeral(int n) {
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

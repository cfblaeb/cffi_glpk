from glpk_cffi import ffi, lib

ia = ffi.new("int[1001]")
ja = ffi.new("int[1001]")
ar = ffi.new("double[1001]")
lp = lib.glp_create_prob()
lib.glp_set_prob_name(lp, b"sample");
lib.glp_set_obj_dir(lp, lib.GLP_MAX);
lib.glp_add_rows(lp, 3);
lib.glp_set_row_name(lp, 1, b"p");
lib.glp_set_row_bnds(lp, 1, lib.GLP_UP, 0.0, 100.0);
lib.glp_set_row_name(lp, 2, b"q");
lib.glp_set_row_bnds(lp, 2, lib.GLP_UP, 0.0, 600.0);
lib.glp_set_row_name(lp, 3, b"r");
lib.glp_set_row_bnds(lp, 3, lib.GLP_UP, 0.0, 300.0);
lib.glp_add_cols(lp, 3);
lib.glp_set_col_name(lp, 1, b"x1");
lib.glp_set_col_bnds(lp, 1, lib.GLP_LO, 0.0, 0.0);
lib.glp_set_obj_coef(lp, 1, 10.0);
lib.glp_set_col_name(lp, 2, b"x2");
lib.glp_set_col_bnds(lp, 2, lib.GLP_LO, 0.0, 0.0);
lib.glp_set_obj_coef(lp, 2, 6.0);
lib.glp_set_col_name(lp, 3, b"x3");
lib.glp_set_col_bnds(lp, 3, lib.GLP_LO, 0.0, 0.0);
lib.glp_set_obj_coef(lp, 3, 4.0);
ia[1] = 1; ja[1] = 1; ar[1] = 1.0; # a[1,1] = 1
ia[2] = 1; ja[2] = 2; ar[2] = 1.0; # a[1,2] = 1
ia[3] = 1; ja[3] = 3; ar[3] = 1.0; # a[1,3] = 1
ia[4] = 2; ja[4] = 1; ar[4] = 10.0; # a[2,1] = 10
ia[5] = 3; ja[5] = 1; ar[5] = 2.0; # a[3,1] = 2
ia[6] = 2; ja[6] = 2; ar[6] = 4.0; # a[2,2] = 4
ia[7] = 3; ja[7] = 2; ar[7] = 2.0; # a[3,2] = 2
ia[8] = 2; ja[8] = 3; ar[8] = 5.0; # a[2,3] = 5
ia[9] = 3; ja[9] = 3; ar[9] = 6.0; # a[3,3] = 6
lib.glp_load_matrix(lp, 9, ia, ja, ar);
lib.glp_simplex(lp, ffi.NULL);
Z = lib.glp_get_obj_val(lp);
x1 = lib.glp_get_col_prim(lp, 1);
x2 = lib.glp_get_col_prim(lp, 2);
x3 = lib.glp_get_col_prim(lp, 3);
print("\nZ = %g; x1 = %g; x2 = %g; x3 = %g\n" % (Z, x1, x2, x3))
lib.glp_delete_prob(lp);
from django.conf.urls import patterns

urlpatterns = patterns('maintenance.views',
	(r'^$', 'index', {}, 'maintenance_index'),
	(r'^prods_without_screenshots$', 'prods_without_screenshots', {}, 'maintenance_prods_without_screenshots'),
	(r'^prods_without_external_links$', 'prods_without_external_links', {}, 'maintenance_prods_without_external_links'),
	(r'^prods_with_dead_amigascne_links$', 'prods_with_dead_amigascne_links', {}, 'maintenance_prods_with_dead_amigascne_links'),
	(r'^prods_with_dead_amiga_nvg_org_links$', 'prods_with_dead_amiga_nvg_org_links', {}, 'maintenance_prods_with_dead_amiga_nvg_org_links'),
	(r'^prods_without_platforms$', 'prods_without_platforms', {}, 'maintenance_prods_without_platforms'),
	(r'^prods_with_blurbs$', 'prods_with_blurbs', {}, 'maintenance_prods_with_blurbs'),
	(r'^prod_comments$', 'prod_comments', {}, 'maintenance_prod_comments'),

	# release dates
	(r'^prod_soundtracks_without_release_date$', 'prod_soundtracks_without_release_date', {}, 'maintenance_prod_soundtracks_without_release_date'),
	(r'^prods_without_release_date$', 'prods_without_release_date', {}, 'maintenance_prods_without_release_date'),
	(r'^prods_without_release_date_with_placement$', 'prods_without_release_date_with_placement', {}, 'maintenance_prods_without_release_date_with_placement'),
	(r'^prods_with_release_date_outside_party$', 'prods_with_release_date_outside_party', {}, 'maintenance_prods_with_release_date_outside_party'),
	(r'^fix_release_dates$', 'fix_release_dates', {}, 'maintenance_fix_release_dates'),

	# cleanup
	(r'^group_nicks_with_brackets$', 'group_nicks_with_brackets', {}, 'maintenance_group_nicks_with_brackets'),
	(r'^ambiguous_groups_with_no_differentiators$', 'ambiguous_groups_with_no_differentiators', {}, 'maintenance_ambiguous_groups_with_no_differentiators'),
	(r'^implied_memberships$', 'implied_memberships', {}, 'maintenance_implied_memberships'),
	(r'^add_membership$', 'add_membership', {}, 'maintenance_add_membership'),
	(r'^sceneorg_party_dirs_with_no_party$', 'sceneorg_party_dirs_with_no_party', {}, 'maintenance_sceneorg_party_dirs_with_no_party'),
	(r'^add_sceneorg_link_to_party$', 'add_sceneorg_link_to_party', {}, 'maintenance_add_sceneorg_link_to_party'),
	(r'^empty_releasers$', 'empty_releasers', {}, 'maintenance_empty_releasers'),
	(r'^public_real_names$', 'public_real_names', {}, 'maintenance_public_real_names'),
	(r'^credits_to_move_to_text$', 'credits_to_move_to_text', {}, 'maintenance_credits_to_move_to_text'),

	# de-duping
	(r'^prods_with_same_named_credits$', 'prods_with_same_named_credits', {}, 'maintenance_prods_with_same_named_credits'),
	(r'^same_named_prods_by_same_releaser$', 'same_named_prods_by_same_releaser', {}, 'maintenance_same_named_prods_by_same_releaser'),
	(r'^same_named_prods_without_special_chars$', 'same_named_prods_without_special_chars', {}, 'maintenance_same_named_prods_without_special_chars'),
	(r'^duplicate_external_links$', 'duplicate_external_links', {}, 'maintenance_duplicate_external_links'),
	(r'^matching_real_names$', 'matching_real_names', {}, 'maintenance_matching_real_names'),
	(r'^matching_surnames$', 'matching_surnames', {}, 'maintenance_matching_surnames'),
	(r'^groups_with_same_named_members$', 'groups_with_same_named_members', {}, 'maintenance_groups_with_same_named_members'),
	(r'^releasers_with_same_named_groups$', 'releasers_with_same_named_groups', {}, 'maintenance_releasers_with_same_named_groups'),

	# parties
	(r'^parties_with_incomplete_dates$', 'parties_with_incomplete_dates', {}, 'maintenance_parties_with_incomplete_dates'),
	(r'^parties_with_no_location$', 'parties_with_no_location', {}, 'maintenance_parties_with_no_location'),
	(r'^result_file_encoding$', 'results_with_no_encoding', {}, 'maintenance_results_with_no_encoding'),
	(r'^result_file_encoding/(\d+)/$', 'fix_results_file_encoding', {}, 'maintenance_fix_results_file_encoding'),

	(r'^exclude$', 'exclude', {}, 'maintenance_exclude'),

	(r'^unresolved_screenshots$', 'unresolved_screenshots', {}, 'maintenance_unresolved_screenshots'),
	(r'^archive_member/(\d+)/$', 'view_archive_member', {}, 'maintenance_view_archive_member'),
	(r'^resolve_screenshot/(\d+)/(\d+)/$', 'resolve_screenshot', {}, 'maintenance_resolve_screenshot'),
)

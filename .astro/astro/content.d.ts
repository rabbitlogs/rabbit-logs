declare module 'astro:content' {
	interface RenderResult {
		Content: import('astro/runtime/server/index.js').AstroComponentFactory;
		headings: import('astro').MarkdownHeading[];
		remarkPluginFrontmatter: Record<string, any>;
	}
	interface Render {
		'.md': Promise<RenderResult>;
	}

	export interface RenderedContent {
		html: string;
		metadata?: {
			imagePaths: Array<string>;
			[key: string]: unknown;
		};
	}
}

declare module 'astro:content' {
	type Flatten<T> = T extends { [K: string]: infer U } ? U : never;

	export type CollectionKey = keyof AnyEntryMap;
	export type CollectionEntry<C extends CollectionKey> = Flatten<AnyEntryMap[C]>;

	export type ContentCollectionKey = keyof ContentEntryMap;
	export type DataCollectionKey = keyof DataEntryMap;

	type AllValuesOf<T> = T extends any ? T[keyof T] : never;
	type ValidContentEntrySlug<C extends keyof ContentEntryMap> = AllValuesOf<
		ContentEntryMap[C]
	>['slug'];

	/** @deprecated Use `getEntry` instead. */
	export function getEntryBySlug<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		// Note that this has to accept a regular string too, for SSR
		entrySlug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;

	/** @deprecated Use `getEntry` instead. */
	export function getDataEntryById<C extends keyof DataEntryMap, E extends keyof DataEntryMap[C]>(
		collection: C,
		entryId: E,
	): Promise<CollectionEntry<C>>;

	export function getCollection<C extends keyof AnyEntryMap, E extends CollectionEntry<C>>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => entry is E,
	): Promise<E[]>;
	export function getCollection<C extends keyof AnyEntryMap>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => unknown,
	): Promise<CollectionEntry<C>[]>;

	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(entry: {
		collection: C;
		slug: E;
	}): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(entry: {
		collection: C;
		id: E;
	}): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		slug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(
		collection: C,
		id: E,
	): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;

	/** Resolve an array of entry references from the same collection */
	export function getEntries<C extends keyof ContentEntryMap>(
		entries: {
			collection: C;
			slug: ValidContentEntrySlug<C>;
		}[],
	): Promise<CollectionEntry<C>[]>;
	export function getEntries<C extends keyof DataEntryMap>(
		entries: {
			collection: C;
			id: keyof DataEntryMap[C];
		}[],
	): Promise<CollectionEntry<C>[]>;

	export function render<C extends keyof AnyEntryMap>(
		entry: AnyEntryMap[C][string],
	): Promise<RenderResult>;

	export function reference<C extends keyof AnyEntryMap>(
		collection: C,
	): import('astro/zod').ZodEffects<
		import('astro/zod').ZodString,
		C extends keyof ContentEntryMap
			? {
					collection: C;
					slug: ValidContentEntrySlug<C>;
				}
			: {
					collection: C;
					id: keyof DataEntryMap[C];
				}
	>;
	// Allow generic `string` to avoid excessive type errors in the config
	// if `dev` is not running to update as you edit.
	// Invalid collection names will be caught at build time.
	export function reference<C extends string>(
		collection: C,
	): import('astro/zod').ZodEffects<import('astro/zod').ZodString, never>;

	type ReturnTypeOrOriginal<T> = T extends (...args: any[]) => infer R ? R : T;
	type InferEntrySchema<C extends keyof AnyEntryMap> = import('astro/zod').infer<
		ReturnTypeOrOriginal<Required<ContentConfig['collections'][C]>['schema']>
	>;

	type ContentEntryMap = {
		"blog": {
"en/sap-certification.md": {
	id: "en/sap-certification.md";
  slug: "en/sap-certification";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"en/sap-cpim.md": {
	id: "en/sap-cpim.md";
  slug: "en/sap-cpim";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"en/sap-exam-format.md": {
	id: "en/sap-exam-format.md";
  slug: "en/sap-exam-format";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"en/sap-font-readability.md": {
	id: "en/sap-font-readability.md";
  slug: "en/sap-font-readability";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"en/sap-signature-theme.md": {
	id: "en/sap-signature-theme.md";
  slug: "en/sap-signature-theme";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"en/sap-what-is-sap.md": {
	id: "en/sap-what-is-sap.md";
  slug: "en/sap-what-is-sap";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-activity-cnf.md": {
	id: "ko/sap-activity-cnf.md";
  slug: "ko/sap-activity-cnf";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-autocomplete.md": {
	id: "ko/sap-autocomplete.md";
  slug: "ko/sap-autocomplete";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-batch-job.md": {
	id: "ko/sap-batch-job.md";
  slug: "ko/sap-batch-job";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-batch-management.md": {
	id: "ko/sap-batch-management.md";
  slug: "ko/sap-batch-management";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-best-practice.md": {
	id: "ko/sap-best-practice.md";
  slug: "ko/sap-best-practice";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-build-project-difficulty.md": {
	id: "ko/sap-build-project-difficulty.md";
  slug: "ko/sap-build-project-difficulty";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-cbo-z-program.md": {
	id: "ko/sap-cbo-z-program.md";
  slug: "ko/sap-cbo-z-program";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-certification.md": {
	id: "ko/sap-certification.md";
  slug: "ko/sap-certification";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-change-management.md": {
	id: "ko/sap-change-management.md";
  slug: "ko/sap-change-management";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-circular-bom.md": {
	id: "ko/sap-circular-bom.md";
  slug: "ko/sap-circular-bom";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-cpim.md": {
	id: "ko/sap-cpim.md";
  slug: "ko/sap-cpim";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-cutover-live.md": {
	id: "ko/sap-cutover-live.md";
  slug: "ko/sap-cutover-live";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-cutover.md": {
	id: "ko/sap-cutover.md";
  slug: "ko/sap-cutover";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-data-types.md": {
	id: "ko/sap-data-types.md";
  slug: "ko/sap-data-types";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-dropdown.md": {
	id: "ko/sap-dropdown.md";
  slug: "ko/sap-dropdown";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-exam-format.md": {
	id: "ko/sap-exam-format.md";
  slug: "ko/sap-exam-format";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-field-names.md": {
	id: "ko/sap-field-names.md";
  slug: "ko/sap-field-names";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-fit-gap.md": {
	id: "ko/sap-fit-gap.md";
  slug: "ko/sap-fit-gap";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-font-readability.md": {
	id: "ko/sap-font-readability.md";
  slug: "ko/sap-font-readability";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-gi-gr-cnf.md": {
	id: "ko/sap-gi-gr-cnf.md";
  slug: "ko/sap-gi-gr-cnf";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-history.md": {
	id: "ko/sap-history.md";
  slug: "ko/sap-history";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-integration-test.md": {
	id: "ko/sap-integration-test.md";
  slug: "ko/sap-integration-test";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-joule-clean-core.md": {
	id: "ko/sap-joule-clean-core.md";
  slug: "ko/sap-joule-clean-core";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-mes-interface.md": {
	id: "ko/sap-mes-interface.md";
  slug: "ko/sap-mes-interface";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-mes-role.md": {
	id: "ko/sap-mes-role.md";
  slug: "ko/sap-mes-role";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-modules-guide.md": {
	id: "ko/sap-modules-guide.md";
  slug: "ko/sap-modules-guide";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-movement-type.md": {
	id: "ko/sap-movement-type.md";
  slug: "ko/sap-movement-type";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-mrp.md": {
	id: "ko/sap-mrp.md";
  slug: "ko/sap-mrp";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-now-ai-tour-2025.md": {
	id: "ko/sap-now-ai-tour-2025.md";
  slug: "ko/sap-now-ai-tour-2025";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-org-structure.md": {
	id: "ko/sap-org-structure.md";
  slug: "ko/sap-org-structure";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-password-asterisk.md": {
	id: "ko/sap-password-asterisk.md";
  slug: "ko/sap-password-asterisk";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-pi-overview.md": {
	id: "ko/sap-pi-overview.md";
  slug: "ko/sap-pi-overview";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-pi-vs-implementation.md": {
	id: "ko/sap-pi-vs-implementation.md";
  slug: "ko/sap-pi-vs-implementation";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-planned-vs-production-order.md": {
	id: "ko/sap-planned-vs-production-order.md";
  slug: "ko/sap-planned-vs-production-order";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-pp-master-data.md": {
	id: "ko/sap-pp-master-data.md";
  slug: "ko/sap-pp-master-data";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-pp-overview.md": {
	id: "ko/sap-pp-overview.md";
  slug: "ko/sap-pp-overview";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-pp-tcode.md": {
	id: "ko/sap-pp-tcode.md";
  slug: "ko/sap-pp-tcode";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-production-order-carryover.md": {
	id: "ko/sap-production-order-carryover.md";
  slug: "ko/sap-production-order-carryover";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-production-order-number.md": {
	id: "ko/sap-production-order-number.md";
  slug: "ko/sap-production-order-number";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-production-order-status.md": {
	id: "ko/sap-production-order-status.md";
  slug: "ko/sap-production-order-status";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-production-strategy.md": {
	id: "ko/sap-production-strategy.md";
  slug: "ko/sap-production-strategy";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-prototype-test.md": {
	id: "ko/sap-prototype-test.md";
  slug: "ko/sap-prototype-test";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-signature-theme.md": {
	id: "ko/sap-signature-theme.md";
  slug: "ko/sap-signature-theme";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-tcode-basics.md": {
	id: "ko/sap-tcode-basics.md";
  slug: "ko/sap-tcode-basics";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-test-overview.md": {
	id: "ko/sap-test-overview.md";
  slug: "ko/sap-test-overview";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-uat.md": {
	id: "ko/sap-uat.md";
  slug: "ko/sap-uat";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-unit-test.md": {
	id: "ko/sap-unit-test.md";
  slug: "ko/sap-unit-test";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-user-parameters.md": {
	id: "ko/sap-user-parameters.md";
  slug: "ko/sap-user-parameters";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-what-is-sap.md": {
	id: "ko/sap-what-is-sap.md";
  slug: "ko/sap-what-is-sap";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/sap-wip.md": {
	id: "ko/sap-wip.md";
  slug: "ko/sap-wip";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/stats-adsp.md": {
	id: "ko/stats-adsp.md";
  slug: "ko/stats-adsp";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/stats-correlation-vs-causation.md": {
	id: "ko/stats-correlation-vs-causation.md";
  slug: "ko/stats-correlation-vs-causation";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/stats-descriptive-basics.md": {
	id: "ko/stats-descriptive-basics.md";
  slug: "ko/stats-descriptive-basics";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/stats-excel-powerquery-pivot.md": {
	id: "ko/stats-excel-powerquery-pivot.md";
  slug: "ko/stats-excel-powerquery-pivot";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/stats-mean-trap-kpi.md": {
	id: "ko/stats-mean-trap-kpi.md";
  slug: "ko/stats-mean-trap-kpi";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/stats-sap-inventory-variance.md": {
	id: "ko/stats-sap-inventory-variance.md";
  slug: "ko/stats-sap-inventory-variance";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/stats-why-back-to-school.md": {
	id: "ko/stats-why-back-to-school.md";
  slug: "ko/stats-why-back-to-school";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/study-pp-routing.md": {
	id: "ko/study-pp-routing.md";
  slug: "ko/study-pp-routing";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
"ko/study-pp-work-center.md": {
	id: "ko/study-pp-work-center.md";
  slug: "ko/study-pp-work-center";
  body: string;
  collection: "blog";
  data: InferEntrySchema<"blog">
} & { render(): Render[".md"] };
};

	};

	type DataEntryMap = {
		
	};

	type AnyEntryMap = ContentEntryMap & DataEntryMap;

	export type ContentConfig = typeof import("./../../src/content/config.js");
}

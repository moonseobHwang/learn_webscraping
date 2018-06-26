package com.mahau.incubate.model;

import java.io.Serializable;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.function.Function;
import java.util.function.ToDoubleFunction;
import java.util.function.ToIntFunction;
import java.util.function.ToLongFunction;

import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.util.Assert;

public class MemberInfo implements UserDetails {

	private static final long serialVersionUID = 1L;

	private String memberID; // Member ID
	private String email; // Member Email
	private String MemberName; // Member Name
	private String password; // Password
	private Set<GrantedAuthority> authorities; // Roles by Member

	public MemberInfo(String memberID, String email, String MemberName,
			String password, Collection<? extends GrantedAuthority> authorities) {
		this.memberID = memberID;
		this.email = email;
		this.MemberName = MemberName;
		this.password = password;
		this.authorities = Collections
				.unmodifiableSet(sortAuthorities(authorities));
	}

	public String getMemberID() {
		return memberID;
	}

	public void setMemberID(String memberID) {
		this.memberID = memberID;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getMemberName() {
		return MemberName;
	}

	public void setMemberName(String memberName) {
		MemberName = memberName;
	}

	@Override
	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	@Override
	public Collection<? extends GrantedAuthority> getAuthorities() {
		return authorities;
	}

	public void setAuthorities(
			Collection<? extends GrantedAuthority> authorities) {
		this.authorities = Collections
				.unmodifiableSet(sortAuthorities(authorities));
	}

	@Override
	public String getUsername() {
		return memberID;
	}

	@Override
	public boolean isAccountNonExpired() {
		return true;
	}

	@Override
	public boolean isAccountNonLocked() {
		return true;
	}

	@Override
	public boolean isCredentialsNonExpired() {
		return true;
	}

	@Override
	public boolean isEnabled() {
		return true;
	}

	private static SortedSet<GrantedAuthority> sortAuthorities(
			Collection<? extends GrantedAuthority> authorities) {
		Assert.notNull(authorities,
				"Cannot pass a null GrantedAuthority collection");
		// Ensure array iteration order is predictable (as per
		// UserDetails.getAuthorities() contract and SEC-717)
		SortedSet<GrantedAuthority> sortedAuthorities = new TreeSet<GrantedAuthority>(
				new AuthorityComparator());

		for (GrantedAuthority grantedAuthority : authorities) {
			Assert.notNull(grantedAuthority,
					"GrantedAuthority list cannot contain any null elements");
			sortedAuthorities.add(grantedAuthority);
		}

		return sortedAuthorities;
	}

	private static class AuthorityComparator implements
			Comparator<GrantedAuthority>, Serializable {

		private static final long serialVersionUID = 1L;

		@Override
		public int compare(GrantedAuthority g1, GrantedAuthority g2) {
			// Neither should ever be null as each entry is checked before
			// adding it to the set.
			// If the authority is null, it is a custom authority and should
			// precede others.
			if (g2.getAuthority() == null) {
				return -1;
			}

			if (g1.getAuthority() == null) {
				return 1;
			}

			return g1.getAuthority().compareTo(g2.getAuthority());
		}

		@Override
		public Comparator<GrantedAuthority> reversed() {
			// TODO Auto-generated method stub
			return null;
		}

		@Override
		public Comparator<GrantedAuthority> thenComparing(
				Comparator<? super GrantedAuthority> other) {
			// TODO Auto-generated method stub
			return null;
		}

		@Override
		public <U> Comparator<GrantedAuthority> thenComparing(
				Function<? super GrantedAuthority, ? extends U> keyExtractor,
				Comparator<? super U> keyComparator) {
			// TODO Auto-generated method stub
			return null;
		}

		@Override
		public <U extends Comparable<? super U>> Comparator<GrantedAuthority> thenComparing(
				Function<? super GrantedAuthority, ? extends U> keyExtractor) {
			// TODO Auto-generated method stub
			return null;
		}

		@Override
		public Comparator<GrantedAuthority> thenComparingInt(
				ToIntFunction<? super GrantedAuthority> keyExtractor) {
			// TODO Auto-generated method stub
			return null;
		}

		@Override
		public Comparator<GrantedAuthority> thenComparingLong(
				ToLongFunction<? super GrantedAuthority> keyExtractor) {
			// TODO Auto-generated method stub
			return null;
		}

		@Override
		public Comparator<GrantedAuthority> thenComparingDouble(
				ToDoubleFunction<? super GrantedAuthority> keyExtractor) {
			// TODO Auto-generated method stub
			return null;
		}

	}
}
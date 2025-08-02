_Z='etsysResourceLimitsProfileTableGroup'
_Y='etsysResourceLimitsProfileGroup'
_X='etsysResourceLimitsProfileL2EgressAcl'
_W='etsysResourceLimitsProfileIpv4EgressAcl'
_V='etsysResourceLimitsProfileIpv6EgressAcl'
_U='etsysResourceLimitsProfileL2IngressAcl'
_T='etsysResourceLimitsProfileIpv4Pbr'
_S='etsysResourceLimitsProfileIpv4IngressAcl'
_R='etsysResourceLimitsProfileIpv6Pbr'
_Q='etsysResourceLimitsProfileIpv6IngressAcl'
_P='etsysResourceLimitsProfileL2Rules'
_O='etsysResourceLimitsProfileIpv4Rules'
_N='etsysResourceLimitsProfileIpv6Rules'
_M='etsysResourceLimitsProfileMacRules'
_L='etsysResourceLimitsProfileAuthenticatedUsers'
_K='etsysResourceLimitsProfileCapabilities'
_J='etsysResourceLimitsProfileOperational'
_I='etsysResourceLimitsProfileAdmin'
_H='etsysResourceLimitsProfileIndex'
_G='switch'
_F='router2'
_E='router1'
_D='default'
_C='read-only'
_B='ENTERASYS-RESOURCE-LIMITS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysResourceLimitsMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,876))
if mibBuilder.loadTexts:etsysResourceLimitsMIB.setRevisions(('2013-12-16 16:22',))
class EtsysResourceLimitsProfiles(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3)))
_EtsysResourceLimitsObjects_ObjectIdentity=ObjectIdentity
etsysResourceLimitsObjects=_EtsysResourceLimitsObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,876,1))
_EtsysResourceLimitsProfile_ObjectIdentity=ObjectIdentity
etsysResourceLimitsProfile=_EtsysResourceLimitsProfile_ObjectIdentity((1,3,6,1,4,1,5624,1,2,876,1,1))
_EtsysResourceLimitsProfileAdmin_Type=EtsysResourceLimitsProfiles
_EtsysResourceLimitsProfileAdmin_Object=MibScalar
etsysResourceLimitsProfileAdmin=_EtsysResourceLimitsProfileAdmin_Object((1,3,6,1,4,1,5624,1,2,876,1,1,1),_EtsysResourceLimitsProfileAdmin_Type())
etsysResourceLimitsProfileAdmin.setMaxAccess('read-write')
if mibBuilder.loadTexts:etsysResourceLimitsProfileAdmin.setStatus(_A)
_EtsysResourceLimitsProfileOperational_Type=EtsysResourceLimitsProfiles
_EtsysResourceLimitsProfileOperational_Object=MibScalar
etsysResourceLimitsProfileOperational=_EtsysResourceLimitsProfileOperational_Object((1,3,6,1,4,1,5624,1,2,876,1,1,2),_EtsysResourceLimitsProfileOperational_Type())
etsysResourceLimitsProfileOperational.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileOperational.setStatus(_A)
class _EtsysResourceLimitsProfileCapabilities_Type(Bits):namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3)))
_EtsysResourceLimitsProfileCapabilities_Type.__name__='Bits'
_EtsysResourceLimitsProfileCapabilities_Object=MibScalar
etsysResourceLimitsProfileCapabilities=_EtsysResourceLimitsProfileCapabilities_Object((1,3,6,1,4,1,5624,1,2,876,1,1,3),_EtsysResourceLimitsProfileCapabilities_Type())
etsysResourceLimitsProfileCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileCapabilities.setStatus(_A)
_EtsysResourceLimitsProfileTable_Object=MibTable
etsysResourceLimitsProfileTable=_EtsysResourceLimitsProfileTable_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4))
if mibBuilder.loadTexts:etsysResourceLimitsProfileTable.setStatus(_A)
_EtsysResourceLimitsProfileEntry_Object=MibTableRow
etsysResourceLimitsProfileEntry=_EtsysResourceLimitsProfileEntry_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1))
etsysResourceLimitsProfileEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:etsysResourceLimitsProfileEntry.setStatus(_A)
_EtsysResourceLimitsProfileIndex_Type=EtsysResourceLimitsProfiles
_EtsysResourceLimitsProfileIndex_Object=MibTableColumn
etsysResourceLimitsProfileIndex=_EtsysResourceLimitsProfileIndex_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,1),_EtsysResourceLimitsProfileIndex_Type())
etsysResourceLimitsProfileIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysResourceLimitsProfileIndex.setStatus(_A)
_EtsysResourceLimitsProfileAuthenticatedUsers_Type=Unsigned32
_EtsysResourceLimitsProfileAuthenticatedUsers_Object=MibTableColumn
etsysResourceLimitsProfileAuthenticatedUsers=_EtsysResourceLimitsProfileAuthenticatedUsers_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,2),_EtsysResourceLimitsProfileAuthenticatedUsers_Type())
etsysResourceLimitsProfileAuthenticatedUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileAuthenticatedUsers.setStatus(_A)
_EtsysResourceLimitsProfileMacRules_Type=Unsigned32
_EtsysResourceLimitsProfileMacRules_Object=MibTableColumn
etsysResourceLimitsProfileMacRules=_EtsysResourceLimitsProfileMacRules_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,3),_EtsysResourceLimitsProfileMacRules_Type())
etsysResourceLimitsProfileMacRules.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileMacRules.setStatus(_A)
_EtsysResourceLimitsProfileIpv6Rules_Type=Unsigned32
_EtsysResourceLimitsProfileIpv6Rules_Object=MibTableColumn
etsysResourceLimitsProfileIpv6Rules=_EtsysResourceLimitsProfileIpv6Rules_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,4),_EtsysResourceLimitsProfileIpv6Rules_Type())
etsysResourceLimitsProfileIpv6Rules.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileIpv6Rules.setStatus(_A)
_EtsysResourceLimitsProfileIpv4Rules_Type=Unsigned32
_EtsysResourceLimitsProfileIpv4Rules_Object=MibTableColumn
etsysResourceLimitsProfileIpv4Rules=_EtsysResourceLimitsProfileIpv4Rules_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,5),_EtsysResourceLimitsProfileIpv4Rules_Type())
etsysResourceLimitsProfileIpv4Rules.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileIpv4Rules.setStatus(_A)
_EtsysResourceLimitsProfileL2Rules_Type=Unsigned32
_EtsysResourceLimitsProfileL2Rules_Object=MibTableColumn
etsysResourceLimitsProfileL2Rules=_EtsysResourceLimitsProfileL2Rules_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,6),_EtsysResourceLimitsProfileL2Rules_Type())
etsysResourceLimitsProfileL2Rules.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileL2Rules.setStatus(_A)
_EtsysResourceLimitsProfileIpv6IngressAcl_Type=Unsigned32
_EtsysResourceLimitsProfileIpv6IngressAcl_Object=MibTableColumn
etsysResourceLimitsProfileIpv6IngressAcl=_EtsysResourceLimitsProfileIpv6IngressAcl_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,7),_EtsysResourceLimitsProfileIpv6IngressAcl_Type())
etsysResourceLimitsProfileIpv6IngressAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileIpv6IngressAcl.setStatus(_A)
_EtsysResourceLimitsProfileIpv6Pbr_Type=Unsigned32
_EtsysResourceLimitsProfileIpv6Pbr_Object=MibTableColumn
etsysResourceLimitsProfileIpv6Pbr=_EtsysResourceLimitsProfileIpv6Pbr_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,8),_EtsysResourceLimitsProfileIpv6Pbr_Type())
etsysResourceLimitsProfileIpv6Pbr.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileIpv6Pbr.setStatus(_A)
_EtsysResourceLimitsProfileIpv4IngressAcl_Type=Unsigned32
_EtsysResourceLimitsProfileIpv4IngressAcl_Object=MibTableColumn
etsysResourceLimitsProfileIpv4IngressAcl=_EtsysResourceLimitsProfileIpv4IngressAcl_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,9),_EtsysResourceLimitsProfileIpv4IngressAcl_Type())
etsysResourceLimitsProfileIpv4IngressAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileIpv4IngressAcl.setStatus(_A)
_EtsysResourceLimitsProfileIpv4Pbr_Type=Unsigned32
_EtsysResourceLimitsProfileIpv4Pbr_Object=MibTableColumn
etsysResourceLimitsProfileIpv4Pbr=_EtsysResourceLimitsProfileIpv4Pbr_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,10),_EtsysResourceLimitsProfileIpv4Pbr_Type())
etsysResourceLimitsProfileIpv4Pbr.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileIpv4Pbr.setStatus(_A)
_EtsysResourceLimitsProfileL2IngressAcl_Type=Unsigned32
_EtsysResourceLimitsProfileL2IngressAcl_Object=MibTableColumn
etsysResourceLimitsProfileL2IngressAcl=_EtsysResourceLimitsProfileL2IngressAcl_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,11),_EtsysResourceLimitsProfileL2IngressAcl_Type())
etsysResourceLimitsProfileL2IngressAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileL2IngressAcl.setStatus(_A)
_EtsysResourceLimitsProfileIpv6EgressAcl_Type=Unsigned32
_EtsysResourceLimitsProfileIpv6EgressAcl_Object=MibTableColumn
etsysResourceLimitsProfileIpv6EgressAcl=_EtsysResourceLimitsProfileIpv6EgressAcl_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,12),_EtsysResourceLimitsProfileIpv6EgressAcl_Type())
etsysResourceLimitsProfileIpv6EgressAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileIpv6EgressAcl.setStatus(_A)
_EtsysResourceLimitsProfileIpv4EgressAcl_Type=Unsigned32
_EtsysResourceLimitsProfileIpv4EgressAcl_Object=MibTableColumn
etsysResourceLimitsProfileIpv4EgressAcl=_EtsysResourceLimitsProfileIpv4EgressAcl_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,13),_EtsysResourceLimitsProfileIpv4EgressAcl_Type())
etsysResourceLimitsProfileIpv4EgressAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileIpv4EgressAcl.setStatus(_A)
_EtsysResourceLimitsProfileL2EgressAcl_Type=Unsigned32
_EtsysResourceLimitsProfileL2EgressAcl_Object=MibTableColumn
etsysResourceLimitsProfileL2EgressAcl=_EtsysResourceLimitsProfileL2EgressAcl_Object((1,3,6,1,4,1,5624,1,2,876,1,1,4,1,14),_EtsysResourceLimitsProfileL2EgressAcl_Type())
etsysResourceLimitsProfileL2EgressAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceLimitsProfileL2EgressAcl.setStatus(_A)
_EtsysResourceLimitsConformance_ObjectIdentity=ObjectIdentity
etsysResourceLimitsConformance=_EtsysResourceLimitsConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,876,2))
_EtsysResourceLimitsGroups_ObjectIdentity=ObjectIdentity
etsysResourceLimitsGroups=_EtsysResourceLimitsGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,876,2,1))
_EtsysResourceLimitsCompliances_ObjectIdentity=ObjectIdentity
etsysResourceLimitsCompliances=_EtsysResourceLimitsCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,876,2,2))
etsysResourceLimitsProfileGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,876,2,1,1))
etsysResourceLimitsProfileGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:etsysResourceLimitsProfileGroup.setStatus(_A)
etsysResourceLimitsProfileTableGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,876,2,1,2))
etsysResourceLimitsProfileTableGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:etsysResourceLimitsProfileTableGroup.setStatus(_A)
etsysResourceLimitsProfileCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,876,2,2,1))
etsysResourceLimitsProfileCompliance.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:etsysResourceLimitsProfileCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EtsysResourceLimitsProfiles':EtsysResourceLimitsProfiles,'etsysResourceLimitsMIB':etsysResourceLimitsMIB,'etsysResourceLimitsObjects':etsysResourceLimitsObjects,'etsysResourceLimitsProfile':etsysResourceLimitsProfile,_I:etsysResourceLimitsProfileAdmin,_J:etsysResourceLimitsProfileOperational,_K:etsysResourceLimitsProfileCapabilities,'etsysResourceLimitsProfileTable':etsysResourceLimitsProfileTable,'etsysResourceLimitsProfileEntry':etsysResourceLimitsProfileEntry,_H:etsysResourceLimitsProfileIndex,_L:etsysResourceLimitsProfileAuthenticatedUsers,_M:etsysResourceLimitsProfileMacRules,_N:etsysResourceLimitsProfileIpv6Rules,_O:etsysResourceLimitsProfileIpv4Rules,_P:etsysResourceLimitsProfileL2Rules,_Q:etsysResourceLimitsProfileIpv6IngressAcl,_R:etsysResourceLimitsProfileIpv6Pbr,_S:etsysResourceLimitsProfileIpv4IngressAcl,_T:etsysResourceLimitsProfileIpv4Pbr,_U:etsysResourceLimitsProfileL2IngressAcl,_V:etsysResourceLimitsProfileIpv6EgressAcl,_W:etsysResourceLimitsProfileIpv4EgressAcl,_X:etsysResourceLimitsProfileL2EgressAcl,'etsysResourceLimitsConformance':etsysResourceLimitsConformance,'etsysResourceLimitsGroups':etsysResourceLimitsGroups,_Y:etsysResourceLimitsProfileGroup,_Z:etsysResourceLimitsProfileTableGroup,'etsysResourceLimitsCompliances':etsysResourceLimitsCompliances,'etsysResourceLimitsProfileCompliance':etsysResourceLimitsProfileCompliance})
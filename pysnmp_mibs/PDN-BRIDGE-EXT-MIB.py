_i='pdnDot1dQinQVlanGroup'
_h='pdnDot1dTrafficProfileMaxRateGroup'
_g='pdnDot1dTrafficProfileBasicGroup'
_f='pdnDot1dBasePortUnknownMulticastForwardingModeGroup'
_e='pdnDot1dBasePortRoleGroup'
_d='pdnDot1dBasePortMaxFdbEntriesGroup'
_c='pdnDot1dBasePortOuterEthertype'
_b='pdnDot1dBasePortOuterPriority'
_a='pdnDot1dBasePortOuterTag'
_Z='pdnDot1dTrafficProfileMaxRate'
_Y='pdnDot1dTrafficProfileMappingIndex'
_X='pdnDot1dTrafficProfileMappingRowStatus'
_W='pdnDot1dTrafficProfileInvIndex'
_V='pdnDot1dTrafficProfileTrafficClass'
_U='pdnDot1dTrafficProfileNbrRefs'
_T='pdnDot1dTrafficProfileRowStatus'
_S='pdnDot1dTrafficProfileNextIndex'
_R='pdnDot1dBasePortUnknownMulticastForwardingMode'
_Q='pdnDot1dBasePortRole'
_P='pdnDot1dBasePortMaxFdbEntries'
_O='pdnDot1dBasePortExtEntry'
_N='pdnDot1dTrafficProfileMappingSubPort'
_M='read-only'
_L='not-accessible'
_K='pdnDot1dTrafficProfileIndex'
_J='SnmpAdminString'
_I='dot1dBasePort'
_H='BRIDGE-MIB'
_G='pdnDot1dTrafficProfileName'
_F='Unsigned32'
_E='read-create'
_D='read-write'
_C='Integer32'
_B='PDN-BRIDGE-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,dot1dBasePortEntry=mibBuilder.importSymbols(_H,_I,'dot1dBasePortEntry')
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
PdnTestAndIncrDerivedIndexTC,=mibBuilder.importSymbols('PDN-TC','PdnTestAndIncrDerivedIndexTC')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr')
pdnBridgeExtMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,58))
if mibBuilder.loadTexts:pdnBridgeExtMIB.setRevisions(('2005-10-26 00:00','2005-10-05 00:00','2005-09-29 00:00','2005-09-12 00:00','2005-08-15 00:00','2004-12-10 00:00'))
_PdnBridgeExtNotifications_ObjectIdentity=ObjectIdentity
pdnBridgeExtNotifications=_PdnBridgeExtNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,58,0))
_PdnBridgeExtObjects_ObjectIdentity=ObjectIdentity
pdnBridgeExtObjects=_PdnBridgeExtObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,58,1))
_PdnDot1dBasePortExtTable_Object=MibTable
pdnDot1dBasePortExtTable=_PdnDot1dBasePortExtTable_Object((1,3,6,1,4,1,1795,2,24,2,58,1,1))
if mibBuilder.loadTexts:pdnDot1dBasePortExtTable.setStatus(_A)
_PdnDot1dBasePortExtEntry_Object=MibTableRow
pdnDot1dBasePortExtEntry=_PdnDot1dBasePortExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,58,1,1,1))
if mibBuilder.loadTexts:pdnDot1dBasePortExtEntry.setStatus(_A)
class _PdnDot1dBasePortMaxFdbEntries_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_PdnDot1dBasePortMaxFdbEntries_Type.__name__=_C
_PdnDot1dBasePortMaxFdbEntries_Object=MibTableColumn
pdnDot1dBasePortMaxFdbEntries=_PdnDot1dBasePortMaxFdbEntries_Object((1,3,6,1,4,1,1795,2,24,2,58,1,1,1,1),_PdnDot1dBasePortMaxFdbEntries_Type())
pdnDot1dBasePortMaxFdbEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDot1dBasePortMaxFdbEntries.setStatus(_A)
class _PdnDot1dBasePortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('subscriber',1),('network',2)))
_PdnDot1dBasePortRole_Type.__name__=_C
_PdnDot1dBasePortRole_Object=MibTableColumn
pdnDot1dBasePortRole=_PdnDot1dBasePortRole_Object((1,3,6,1,4,1,1795,2,24,2,58,1,1,1,2),_PdnDot1dBasePortRole_Type())
pdnDot1dBasePortRole.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDot1dBasePortRole.setStatus(_A)
class _PdnDot1dBasePortUnknownMulticastForwardingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('flood',1),('drop',2)))
_PdnDot1dBasePortUnknownMulticastForwardingMode_Type.__name__=_C
_PdnDot1dBasePortUnknownMulticastForwardingMode_Object=MibTableColumn
pdnDot1dBasePortUnknownMulticastForwardingMode=_PdnDot1dBasePortUnknownMulticastForwardingMode_Object((1,3,6,1,4,1,1795,2,24,2,58,1,1,1,3),_PdnDot1dBasePortUnknownMulticastForwardingMode_Type())
pdnDot1dBasePortUnknownMulticastForwardingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDot1dBasePortUnknownMulticastForwardingMode.setStatus(_A)
class _PdnDot1dBasePortOuterTag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_PdnDot1dBasePortOuterTag_Type.__name__=_C
_PdnDot1dBasePortOuterTag_Object=MibTableColumn
pdnDot1dBasePortOuterTag=_PdnDot1dBasePortOuterTag_Object((1,3,6,1,4,1,1795,2,24,2,58,1,1,1,4),_PdnDot1dBasePortOuterTag_Type())
pdnDot1dBasePortOuterTag.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDot1dBasePortOuterTag.setStatus(_A)
class _PdnDot1dBasePortOuterPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PdnDot1dBasePortOuterPriority_Type.__name__=_C
_PdnDot1dBasePortOuterPriority_Object=MibTableColumn
pdnDot1dBasePortOuterPriority=_PdnDot1dBasePortOuterPriority_Object((1,3,6,1,4,1,1795,2,24,2,58,1,1,1,5),_PdnDot1dBasePortOuterPriority_Type())
pdnDot1dBasePortOuterPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDot1dBasePortOuterPriority.setStatus(_A)
class _PdnDot1dBasePortOuterEthertype_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PdnDot1dBasePortOuterEthertype_Type.__name__=_C
_PdnDot1dBasePortOuterEthertype_Object=MibTableColumn
pdnDot1dBasePortOuterEthertype=_PdnDot1dBasePortOuterEthertype_Object((1,3,6,1,4,1,1795,2,24,2,58,1,1,1,6),_PdnDot1dBasePortOuterEthertype_Type())
pdnDot1dBasePortOuterEthertype.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDot1dBasePortOuterEthertype.setStatus(_A)
_PdnDot1dTrafficProfile_ObjectIdentity=ObjectIdentity
pdnDot1dTrafficProfile=_PdnDot1dTrafficProfile_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,58,1,2))
_PdnDot1dTrafficProfileNextIndex_Type=TestAndIncr
_PdnDot1dTrafficProfileNextIndex_Object=MibScalar
pdnDot1dTrafficProfileNextIndex=_PdnDot1dTrafficProfileNextIndex_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,1),_PdnDot1dTrafficProfileNextIndex_Type())
pdnDot1dTrafficProfileNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDot1dTrafficProfileNextIndex.setStatus(_A)
_PdnDot1dTrafficProfileTable_Object=MibTable
pdnDot1dTrafficProfileTable=_PdnDot1dTrafficProfileTable_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,2))
if mibBuilder.loadTexts:pdnDot1dTrafficProfileTable.setStatus(_A)
_PdnDot1dTrafficProfileEntry_Object=MibTableRow
pdnDot1dTrafficProfileEntry=_PdnDot1dTrafficProfileEntry_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,2,1))
pdnDot1dTrafficProfileEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:pdnDot1dTrafficProfileEntry.setStatus(_A)
_PdnDot1dTrafficProfileIndex_Type=PdnTestAndIncrDerivedIndexTC
_PdnDot1dTrafficProfileIndex_Object=MibTableColumn
pdnDot1dTrafficProfileIndex=_PdnDot1dTrafficProfileIndex_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,2,1,1),_PdnDot1dTrafficProfileIndex_Type())
pdnDot1dTrafficProfileIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:pdnDot1dTrafficProfileIndex.setStatus(_A)
_PdnDot1dTrafficProfileRowStatus_Type=RowStatus
_PdnDot1dTrafficProfileRowStatus_Object=MibTableColumn
pdnDot1dTrafficProfileRowStatus=_PdnDot1dTrafficProfileRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,2,1,2),_PdnDot1dTrafficProfileRowStatus_Type())
pdnDot1dTrafficProfileRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDot1dTrafficProfileRowStatus.setStatus(_A)
class _PdnDot1dTrafficProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PdnDot1dTrafficProfileName_Type.__name__=_J
_PdnDot1dTrafficProfileName_Object=MibTableColumn
pdnDot1dTrafficProfileName=_PdnDot1dTrafficProfileName_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,2,1,3),_PdnDot1dTrafficProfileName_Type())
pdnDot1dTrafficProfileName.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDot1dTrafficProfileName.setStatus(_A)
class _PdnDot1dTrafficProfileNbrRefs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PdnDot1dTrafficProfileNbrRefs_Type.__name__=_F
_PdnDot1dTrafficProfileNbrRefs_Object=MibTableColumn
pdnDot1dTrafficProfileNbrRefs=_PdnDot1dTrafficProfileNbrRefs_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,2,1,4),_PdnDot1dTrafficProfileNbrRefs_Type())
pdnDot1dTrafficProfileNbrRefs.setMaxAccess(_M)
if mibBuilder.loadTexts:pdnDot1dTrafficProfileNbrRefs.setStatus(_A)
class _PdnDot1dTrafficProfileTrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('data',1),('video',2),('voice',3)))
_PdnDot1dTrafficProfileTrafficClass_Type.__name__=_C
_PdnDot1dTrafficProfileTrafficClass_Object=MibTableColumn
pdnDot1dTrafficProfileTrafficClass=_PdnDot1dTrafficProfileTrafficClass_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,2,1,5),_PdnDot1dTrafficProfileTrafficClass_Type())
pdnDot1dTrafficProfileTrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDot1dTrafficProfileTrafficClass.setStatus(_A)
class _PdnDot1dTrafficProfileMaxRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_PdnDot1dTrafficProfileMaxRate_Type.__name__=_F
_PdnDot1dTrafficProfileMaxRate_Object=MibTableColumn
pdnDot1dTrafficProfileMaxRate=_PdnDot1dTrafficProfileMaxRate_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,2,1,6),_PdnDot1dTrafficProfileMaxRate_Type())
pdnDot1dTrafficProfileMaxRate.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDot1dTrafficProfileMaxRate.setStatus(_A)
if mibBuilder.loadTexts:pdnDot1dTrafficProfileMaxRate.setUnits('bps')
_PdnDot1dTrafficProfileInvMappingTable_Object=MibTable
pdnDot1dTrafficProfileInvMappingTable=_PdnDot1dTrafficProfileInvMappingTable_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,3))
if mibBuilder.loadTexts:pdnDot1dTrafficProfileInvMappingTable.setStatus(_A)
_PdnDot1dTrafficProfileInvMappingEntry_Object=MibTableRow
pdnDot1dTrafficProfileInvMappingEntry=_PdnDot1dTrafficProfileInvMappingEntry_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,3,1))
pdnDot1dTrafficProfileInvMappingEntry.setIndexNames((1,_B,_G))
if mibBuilder.loadTexts:pdnDot1dTrafficProfileInvMappingEntry.setStatus(_A)
_PdnDot1dTrafficProfileInvIndex_Type=PdnTestAndIncrDerivedIndexTC
_PdnDot1dTrafficProfileInvIndex_Object=MibTableColumn
pdnDot1dTrafficProfileInvIndex=_PdnDot1dTrafficProfileInvIndex_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,3,1,1),_PdnDot1dTrafficProfileInvIndex_Type())
pdnDot1dTrafficProfileInvIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:pdnDot1dTrafficProfileInvIndex.setStatus(_A)
_PdnDot1dTrafficProfileMappingTable_Object=MibTable
pdnDot1dTrafficProfileMappingTable=_PdnDot1dTrafficProfileMappingTable_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,4))
if mibBuilder.loadTexts:pdnDot1dTrafficProfileMappingTable.setStatus(_A)
_PdnDot1dTrafficProfileMappingEntry_Object=MibTableRow
pdnDot1dTrafficProfileMappingEntry=_PdnDot1dTrafficProfileMappingEntry_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,4,1))
pdnDot1dTrafficProfileMappingEntry.setIndexNames((0,_H,_I),(0,_B,_N))
if mibBuilder.loadTexts:pdnDot1dTrafficProfileMappingEntry.setStatus(_A)
class _PdnDot1dTrafficProfileMappingSubPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PdnDot1dTrafficProfileMappingSubPort_Type.__name__=_C
_PdnDot1dTrafficProfileMappingSubPort_Object=MibTableColumn
pdnDot1dTrafficProfileMappingSubPort=_PdnDot1dTrafficProfileMappingSubPort_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,4,1,1),_PdnDot1dTrafficProfileMappingSubPort_Type())
pdnDot1dTrafficProfileMappingSubPort.setMaxAccess(_L)
if mibBuilder.loadTexts:pdnDot1dTrafficProfileMappingSubPort.setStatus(_A)
_PdnDot1dTrafficProfileMappingRowStatus_Type=RowStatus
_PdnDot1dTrafficProfileMappingRowStatus_Object=MibTableColumn
pdnDot1dTrafficProfileMappingRowStatus=_PdnDot1dTrafficProfileMappingRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,4,1,2),_PdnDot1dTrafficProfileMappingRowStatus_Type())
pdnDot1dTrafficProfileMappingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDot1dTrafficProfileMappingRowStatus.setStatus(_A)
_PdnDot1dTrafficProfileMappingIndex_Type=PdnTestAndIncrDerivedIndexTC
_PdnDot1dTrafficProfileMappingIndex_Object=MibTableColumn
pdnDot1dTrafficProfileMappingIndex=_PdnDot1dTrafficProfileMappingIndex_Object((1,3,6,1,4,1,1795,2,24,2,58,1,2,4,1,3),_PdnDot1dTrafficProfileMappingIndex_Type())
pdnDot1dTrafficProfileMappingIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDot1dTrafficProfileMappingIndex.setStatus(_A)
_PdnBridgeExtAFNs_ObjectIdentity=ObjectIdentity
pdnBridgeExtAFNs=_PdnBridgeExtAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,58,2))
_PdnBridgeExtConformance_ObjectIdentity=ObjectIdentity
pdnBridgeExtConformance=_PdnBridgeExtConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,58,3))
_PdnBridgeExtCompliances_ObjectIdentity=ObjectIdentity
pdnBridgeExtCompliances=_PdnBridgeExtCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,58,3,1))
_PdnBridgeExtGroups_ObjectIdentity=ObjectIdentity
pdnBridgeExtGroups=_PdnBridgeExtGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,58,3,2))
_PdnBridgeExtObjGroups_ObjectIdentity=ObjectIdentity
pdnBridgeExtObjGroups=_PdnBridgeExtObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,58,3,2,1))
_PdnBridgeExtTPGroups_ObjectIdentity=ObjectIdentity
pdnBridgeExtTPGroups=_PdnBridgeExtTPGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,58,3,2,1,4))
_PdnBridgeExtAfnGroups_ObjectIdentity=ObjectIdentity
pdnBridgeExtAfnGroups=_PdnBridgeExtAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,58,3,2,2))
_PdnBridgeExtNtfyGroups_ObjectIdentity=ObjectIdentity
pdnBridgeExtNtfyGroups=_PdnBridgeExtNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,58,3,2,3))
dot1dBasePortEntry.registerAugmentions((_B,_O))
pdnDot1dBasePortExtEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
pdnDot1dBasePortMaxFdbEntriesGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,58,3,2,1,1))
pdnDot1dBasePortMaxFdbEntriesGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:pdnDot1dBasePortMaxFdbEntriesGroup.setStatus(_A)
pdnDot1dBasePortRoleGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,58,3,2,1,2))
pdnDot1dBasePortRoleGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:pdnDot1dBasePortRoleGroup.setStatus(_A)
pdnDot1dBasePortUnknownMulticastForwardingModeGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,58,3,2,1,3))
pdnDot1dBasePortUnknownMulticastForwardingModeGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:pdnDot1dBasePortUnknownMulticastForwardingModeGroup.setStatus(_A)
pdnDot1dTrafficProfileBasicGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,58,3,2,1,4,1))
pdnDot1dTrafficProfileBasicGroup.setObjects(*((_B,_S),(_B,_G),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:pdnDot1dTrafficProfileBasicGroup.setStatus(_A)
pdnDot1dTrafficProfileMaxRateGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,58,3,2,1,4,2))
pdnDot1dTrafficProfileMaxRateGroup.setObjects((_B,_Z))
if mibBuilder.loadTexts:pdnDot1dTrafficProfileMaxRateGroup.setStatus(_A)
pdnDot1dQinQVlanGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,58,3,2,1,5))
pdnDot1dQinQVlanGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:pdnDot1dQinQVlanGroup.setStatus(_A)
pdnBridgeExtCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,58,3,1,1))
pdnBridgeExtCompliance.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:pdnBridgeExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnBridgeExtMIB':pdnBridgeExtMIB,'pdnBridgeExtNotifications':pdnBridgeExtNotifications,'pdnBridgeExtObjects':pdnBridgeExtObjects,'pdnDot1dBasePortExtTable':pdnDot1dBasePortExtTable,_O:pdnDot1dBasePortExtEntry,_P:pdnDot1dBasePortMaxFdbEntries,_Q:pdnDot1dBasePortRole,_R:pdnDot1dBasePortUnknownMulticastForwardingMode,_a:pdnDot1dBasePortOuterTag,_b:pdnDot1dBasePortOuterPriority,_c:pdnDot1dBasePortOuterEthertype,'pdnDot1dTrafficProfile':pdnDot1dTrafficProfile,_S:pdnDot1dTrafficProfileNextIndex,'pdnDot1dTrafficProfileTable':pdnDot1dTrafficProfileTable,'pdnDot1dTrafficProfileEntry':pdnDot1dTrafficProfileEntry,_K:pdnDot1dTrafficProfileIndex,_T:pdnDot1dTrafficProfileRowStatus,_G:pdnDot1dTrafficProfileName,_U:pdnDot1dTrafficProfileNbrRefs,_V:pdnDot1dTrafficProfileTrafficClass,_Z:pdnDot1dTrafficProfileMaxRate,'pdnDot1dTrafficProfileInvMappingTable':pdnDot1dTrafficProfileInvMappingTable,'pdnDot1dTrafficProfileInvMappingEntry':pdnDot1dTrafficProfileInvMappingEntry,_W:pdnDot1dTrafficProfileInvIndex,'pdnDot1dTrafficProfileMappingTable':pdnDot1dTrafficProfileMappingTable,'pdnDot1dTrafficProfileMappingEntry':pdnDot1dTrafficProfileMappingEntry,_N:pdnDot1dTrafficProfileMappingSubPort,_X:pdnDot1dTrafficProfileMappingRowStatus,_Y:pdnDot1dTrafficProfileMappingIndex,'pdnBridgeExtAFNs':pdnBridgeExtAFNs,'pdnBridgeExtConformance':pdnBridgeExtConformance,'pdnBridgeExtCompliances':pdnBridgeExtCompliances,'pdnBridgeExtCompliance':pdnBridgeExtCompliance,'pdnBridgeExtGroups':pdnBridgeExtGroups,'pdnBridgeExtObjGroups':pdnBridgeExtObjGroups,_d:pdnDot1dBasePortMaxFdbEntriesGroup,_e:pdnDot1dBasePortRoleGroup,_f:pdnDot1dBasePortUnknownMulticastForwardingModeGroup,'pdnBridgeExtTPGroups':pdnBridgeExtTPGroups,_g:pdnDot1dTrafficProfileBasicGroup,_h:pdnDot1dTrafficProfileMaxRateGroup,_i:pdnDot1dQinQVlanGroup,'pdnBridgeExtAfnGroups':pdnBridgeExtAfnGroups,'pdnBridgeExtNtfyGroups':pdnBridgeExtNtfyGroups})
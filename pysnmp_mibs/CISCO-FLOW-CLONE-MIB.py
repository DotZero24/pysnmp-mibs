_j='cfcFlowStatsGroup'
_i='cfcFlowGroup'
_h='cfcCloneProfileGroup'
_g='cfcFlowOctets'
_f='cfcFlowPkts'
_e='cfcFlowIpCreateTime'
_d='cfcFlowIpAddrDst'
_c='cfcFlowIpAddrDstType'
_b='cfcFlowIpAddrSrc'
_a='cfcFlowIpAddrSrcType'
_Z='cfcFlowIpStorageType'
_Y='cfcFlowIpStatus'
_X='cfcCloneProfileTableChanged'
_W='cfcCloneProfileEgressIf'
_V='cfcCloneProfileEgressIfType'
_U='cfcCloneTargetIfIndex'
_T='cfcCloneTargetType'
_S='cfcCloneProfileFlowType'
_R='cfcCloneProfileFlowCount'
_Q='cfcCloneProfileCreateTime'
_P='cfcCloneProfileDescription'
_O='cfcCloneProfileName'
_N='cfcCloneProfileStorageType'
_M='cfcCloneProfileStatus'
_L='cfcCloneProfileIdNext'
_K='not-accessible'
_J='interface'
_I='SnmpAdminString'
_H='cfcFlowIndex'
_G='StorageType'
_F='cfcCloneProfileId'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='CISCO-FLOW-CLONE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_G,'TextualConvention','TimeStamp')
ciscoFlowCloneMIB=ModuleIdentity((1,3,6,1,4,1,9,9,765))
if mibBuilder.loadTexts:ciscoFlowCloneMIB.setRevisions(('2010-07-08 00:00',))
class CloneProfileIdentifier(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CloneFlowIdentifier(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CloneProfilePointType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('unknown',2),('none',3),(_J,4)))
class CloneProfilePointIdentifier(InterfaceIndexOrZero):status=_A
_CiscoFlowCloneMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoFlowCloneMIBNotifications=_CiscoFlowCloneMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,765,0))
_CiscoFlowCloneMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFlowCloneMIBObjects=_CiscoFlowCloneMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,765,1))
_CfcCloneProfiles_ObjectIdentity=ObjectIdentity
cfcCloneProfiles=_CfcCloneProfiles_ObjectIdentity((1,3,6,1,4,1,9,9,765,1,1))
_CfcCloneProfileIdNext_Type=CloneProfileIdentifier
_CfcCloneProfileIdNext_Object=MibScalar
cfcCloneProfileIdNext=_CfcCloneProfileIdNext_Object((1,3,6,1,4,1,9,9,765,1,1,1),_CfcCloneProfileIdNext_Type())
cfcCloneProfileIdNext.setMaxAccess(_D)
if mibBuilder.loadTexts:cfcCloneProfileIdNext.setStatus(_A)
_CfcCloneProfileTable_Object=MibTable
cfcCloneProfileTable=_CfcCloneProfileTable_Object((1,3,6,1,4,1,9,9,765,1,1,2))
if mibBuilder.loadTexts:cfcCloneProfileTable.setStatus(_A)
_CfcCloneProfileEntry_Object=MibTableRow
cfcCloneProfileEntry=_CfcCloneProfileEntry_Object((1,3,6,1,4,1,9,9,765,1,1,2,1))
cfcCloneProfileEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cfcCloneProfileEntry.setStatus(_A)
_CfcCloneProfileId_Type=CloneProfileIdentifier
_CfcCloneProfileId_Object=MibTableColumn
cfcCloneProfileId=_CfcCloneProfileId_Object((1,3,6,1,4,1,9,9,765,1,1,2,1,1),_CfcCloneProfileId_Type())
cfcCloneProfileId.setMaxAccess(_K)
if mibBuilder.loadTexts:cfcCloneProfileId.setStatus(_A)
_CfcCloneProfileStatus_Type=RowStatus
_CfcCloneProfileStatus_Object=MibTableColumn
cfcCloneProfileStatus=_CfcCloneProfileStatus_Object((1,3,6,1,4,1,9,9,765,1,1,2,1,2),_CfcCloneProfileStatus_Type())
cfcCloneProfileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcCloneProfileStatus.setStatus(_A)
class _CfcCloneProfileStorageType_Type(StorageType):defaultValue=2
_CfcCloneProfileStorageType_Type.__name__=_G
_CfcCloneProfileStorageType_Object=MibTableColumn
cfcCloneProfileStorageType=_CfcCloneProfileStorageType_Object((1,3,6,1,4,1,9,9,765,1,1,2,1,3),_CfcCloneProfileStorageType_Type())
cfcCloneProfileStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcCloneProfileStorageType.setStatus(_A)
class _CfcCloneProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CfcCloneProfileName_Type.__name__=_I
_CfcCloneProfileName_Object=MibTableColumn
cfcCloneProfileName=_CfcCloneProfileName_Object((1,3,6,1,4,1,9,9,765,1,1,2,1,4),_CfcCloneProfileName_Type())
cfcCloneProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcCloneProfileName.setStatus(_A)
_CfcCloneProfileDescription_Type=SnmpAdminString
_CfcCloneProfileDescription_Object=MibTableColumn
cfcCloneProfileDescription=_CfcCloneProfileDescription_Object((1,3,6,1,4,1,9,9,765,1,1,2,1,5),_CfcCloneProfileDescription_Type())
cfcCloneProfileDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcCloneProfileDescription.setStatus(_A)
_CfcCloneProfileCreateTime_Type=TimeStamp
_CfcCloneProfileCreateTime_Object=MibTableColumn
cfcCloneProfileCreateTime=_CfcCloneProfileCreateTime_Object((1,3,6,1,4,1,9,9,765,1,1,2,1,6),_CfcCloneProfileCreateTime_Type())
cfcCloneProfileCreateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cfcCloneProfileCreateTime.setStatus(_A)
_CfcCloneProfileFlowCount_Type=Gauge32
_CfcCloneProfileFlowCount_Object=MibTableColumn
cfcCloneProfileFlowCount=_CfcCloneProfileFlowCount_Object((1,3,6,1,4,1,9,9,765,1,1,2,1,7),_CfcCloneProfileFlowCount_Type())
cfcCloneProfileFlowCount.setMaxAccess(_D)
if mibBuilder.loadTexts:cfcCloneProfileFlowCount.setStatus(_A)
if mibBuilder.loadTexts:cfcCloneProfileFlowCount.setUnits('traffic flows')
class _CfcCloneProfileFlowType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ip',1))
_CfcCloneProfileFlowType_Type.__name__=_E
_CfcCloneProfileFlowType_Object=MibTableColumn
cfcCloneProfileFlowType=_CfcCloneProfileFlowType_Object((1,3,6,1,4,1,9,9,765,1,1,2,1,8),_CfcCloneProfileFlowType_Type())
cfcCloneProfileFlowType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcCloneProfileFlowType.setStatus(_A)
class _CfcCloneTargetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('system',2),(_J,3)))
_CfcCloneTargetType_Type.__name__=_E
_CfcCloneTargetType_Object=MibTableColumn
cfcCloneTargetType=_CfcCloneTargetType_Object((1,3,6,1,4,1,9,9,765,1,1,2,1,9),_CfcCloneTargetType_Type())
cfcCloneTargetType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcCloneTargetType.setStatus(_A)
class _CfcCloneTargetIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CfcCloneTargetIfIndex_Type.__name__=_E
_CfcCloneTargetIfIndex_Object=MibTableColumn
cfcCloneTargetIfIndex=_CfcCloneTargetIfIndex_Object((1,3,6,1,4,1,9,9,765,1,1,2,1,10),_CfcCloneTargetIfIndex_Type())
cfcCloneTargetIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcCloneTargetIfIndex.setStatus(_A)
_CfcCloneProfileEgressIfType_Type=CloneProfilePointType
_CfcCloneProfileEgressIfType_Object=MibTableColumn
cfcCloneProfileEgressIfType=_CfcCloneProfileEgressIfType_Object((1,3,6,1,4,1,9,9,765,1,1,2,1,11),_CfcCloneProfileEgressIfType_Type())
cfcCloneProfileEgressIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcCloneProfileEgressIfType.setStatus(_A)
_CfcCloneProfileEgressIf_Type=CloneProfilePointIdentifier
_CfcCloneProfileEgressIf_Object=MibTableColumn
cfcCloneProfileEgressIf=_CfcCloneProfileEgressIf_Object((1,3,6,1,4,1,9,9,765,1,1,2,1,12),_CfcCloneProfileEgressIf_Type())
cfcCloneProfileEgressIf.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcCloneProfileEgressIf.setStatus(_A)
_CfcCloneProfileTableChanged_Type=TimeStamp
_CfcCloneProfileTableChanged_Object=MibScalar
cfcCloneProfileTableChanged=_CfcCloneProfileTableChanged_Object((1,3,6,1,4,1,9,9,765,1,1,3),_CfcCloneProfileTableChanged_Type())
cfcCloneProfileTableChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:cfcCloneProfileTableChanged.setStatus(_A)
_CfcFlows_ObjectIdentity=ObjectIdentity
cfcFlows=_CfcFlows_ObjectIdentity((1,3,6,1,4,1,9,9,765,1,2))
_CfcFlowIpTable_Object=MibTable
cfcFlowIpTable=_CfcFlowIpTable_Object((1,3,6,1,4,1,9,9,765,1,2,1))
if mibBuilder.loadTexts:cfcFlowIpTable.setStatus(_A)
_CfcFlowIpEntry_Object=MibTableRow
cfcFlowIpEntry=_CfcFlowIpEntry_Object((1,3,6,1,4,1,9,9,765,1,2,1,1))
cfcFlowIpEntry.setIndexNames((0,_B,_F),(0,_B,_H))
if mibBuilder.loadTexts:cfcFlowIpEntry.setStatus(_A)
_CfcFlowIndex_Type=CloneFlowIdentifier
_CfcFlowIndex_Object=MibTableColumn
cfcFlowIndex=_CfcFlowIndex_Object((1,3,6,1,4,1,9,9,765,1,2,1,1,1),_CfcFlowIndex_Type())
cfcFlowIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:cfcFlowIndex.setStatus(_A)
_CfcFlowIpStatus_Type=RowStatus
_CfcFlowIpStatus_Object=MibTableColumn
cfcFlowIpStatus=_CfcFlowIpStatus_Object((1,3,6,1,4,1,9,9,765,1,2,1,1,2),_CfcFlowIpStatus_Type())
cfcFlowIpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFlowIpStatus.setStatus(_A)
class _CfcFlowIpStorageType_Type(StorageType):defaultValue=2
_CfcFlowIpStorageType_Type.__name__=_G
_CfcFlowIpStorageType_Object=MibTableColumn
cfcFlowIpStorageType=_CfcFlowIpStorageType_Object((1,3,6,1,4,1,9,9,765,1,2,1,1,3),_CfcFlowIpStorageType_Type())
cfcFlowIpStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFlowIpStorageType.setStatus(_A)
_CfcFlowIpAddrSrcType_Type=InetAddressType
_CfcFlowIpAddrSrcType_Object=MibTableColumn
cfcFlowIpAddrSrcType=_CfcFlowIpAddrSrcType_Object((1,3,6,1,4,1,9,9,765,1,2,1,1,4),_CfcFlowIpAddrSrcType_Type())
cfcFlowIpAddrSrcType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFlowIpAddrSrcType.setStatus(_A)
_CfcFlowIpAddrSrc_Type=InetAddress
_CfcFlowIpAddrSrc_Object=MibTableColumn
cfcFlowIpAddrSrc=_CfcFlowIpAddrSrc_Object((1,3,6,1,4,1,9,9,765,1,2,1,1,5),_CfcFlowIpAddrSrc_Type())
cfcFlowIpAddrSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFlowIpAddrSrc.setStatus(_A)
_CfcFlowIpAddrDstType_Type=InetAddressType
_CfcFlowIpAddrDstType_Object=MibTableColumn
cfcFlowIpAddrDstType=_CfcFlowIpAddrDstType_Object((1,3,6,1,4,1,9,9,765,1,2,1,1,6),_CfcFlowIpAddrDstType_Type())
cfcFlowIpAddrDstType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFlowIpAddrDstType.setStatus(_A)
_CfcFlowIpAddrDst_Type=InetAddress
_CfcFlowIpAddrDst_Object=MibTableColumn
cfcFlowIpAddrDst=_CfcFlowIpAddrDst_Object((1,3,6,1,4,1,9,9,765,1,2,1,1,7),_CfcFlowIpAddrDst_Type())
cfcFlowIpAddrDst.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFlowIpAddrDst.setStatus(_A)
_CfcFlowIpCreateTime_Type=TimeStamp
_CfcFlowIpCreateTime_Object=MibTableColumn
cfcFlowIpCreateTime=_CfcFlowIpCreateTime_Object((1,3,6,1,4,1,9,9,765,1,2,1,1,8),_CfcFlowIpCreateTime_Type())
cfcFlowIpCreateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cfcFlowIpCreateTime.setStatus(_A)
_CfcFlowStats_ObjectIdentity=ObjectIdentity
cfcFlowStats=_CfcFlowStats_ObjectIdentity((1,3,6,1,4,1,9,9,765,1,3))
_CfcFlowStatsTable_Object=MibTable
cfcFlowStatsTable=_CfcFlowStatsTable_Object((1,3,6,1,4,1,9,9,765,1,3,1))
if mibBuilder.loadTexts:cfcFlowStatsTable.setStatus(_A)
_CfcFlowStatsEntry_Object=MibTableRow
cfcFlowStatsEntry=_CfcFlowStatsEntry_Object((1,3,6,1,4,1,9,9,765,1,3,1,1))
cfcFlowStatsEntry.setIndexNames((0,_B,_F),(0,_B,_H))
if mibBuilder.loadTexts:cfcFlowStatsEntry.setStatus(_A)
_CfcFlowPkts_Type=Counter64
_CfcFlowPkts_Object=MibTableColumn
cfcFlowPkts=_CfcFlowPkts_Object((1,3,6,1,4,1,9,9,765,1,3,1,1,1),_CfcFlowPkts_Type())
cfcFlowPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:cfcFlowPkts.setStatus(_A)
if mibBuilder.loadTexts:cfcFlowPkts.setUnits('packets')
_CfcFlowOctets_Type=Counter64
_CfcFlowOctets_Object=MibTableColumn
cfcFlowOctets=_CfcFlowOctets_Object((1,3,6,1,4,1,9,9,765,1,3,1,1,2),_CfcFlowOctets_Type())
cfcFlowOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:cfcFlowOctets.setStatus(_A)
if mibBuilder.loadTexts:cfcFlowOctets.setUnits('octets')
_CiscoFlowCloneMIBConformance_ObjectIdentity=ObjectIdentity
ciscoFlowCloneMIBConformance=_CiscoFlowCloneMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,765,2))
_CiscoFlowCloneMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFlowCloneMIBCompliances=_CiscoFlowCloneMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,765,2,1))
_CiscoFlowCloneMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFlowCloneMIBGroups=_CiscoFlowCloneMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,765,2,2))
cfcCloneProfileGroup=ObjectGroup((1,3,6,1,4,1,9,9,765,2,2,1))
cfcCloneProfileGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:cfcCloneProfileGroup.setStatus(_A)
cfcFlowGroup=ObjectGroup((1,3,6,1,4,1,9,9,765,2,2,2))
cfcFlowGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:cfcFlowGroup.setStatus(_A)
cfcFlowStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,765,2,2,3))
cfcFlowStatsGroup.setObjects(*((_B,_f),(_B,_g)))
if mibBuilder.loadTexts:cfcFlowStatsGroup.setStatus(_A)
ciscoCloneFlowCompliance01=ModuleCompliance((1,3,6,1,4,1,9,9,765,2,1,1))
ciscoCloneFlowCompliance01.setObjects(*((_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:ciscoCloneFlowCompliance01.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CloneProfileIdentifier':CloneProfileIdentifier,'CloneFlowIdentifier':CloneFlowIdentifier,'CloneProfilePointType':CloneProfilePointType,'CloneProfilePointIdentifier':CloneProfilePointIdentifier,'ciscoFlowCloneMIB':ciscoFlowCloneMIB,'ciscoFlowCloneMIBNotifications':ciscoFlowCloneMIBNotifications,'ciscoFlowCloneMIBObjects':ciscoFlowCloneMIBObjects,'cfcCloneProfiles':cfcCloneProfiles,_L:cfcCloneProfileIdNext,'cfcCloneProfileTable':cfcCloneProfileTable,'cfcCloneProfileEntry':cfcCloneProfileEntry,_F:cfcCloneProfileId,_M:cfcCloneProfileStatus,_N:cfcCloneProfileStorageType,_O:cfcCloneProfileName,_P:cfcCloneProfileDescription,_Q:cfcCloneProfileCreateTime,_R:cfcCloneProfileFlowCount,_S:cfcCloneProfileFlowType,_T:cfcCloneTargetType,_U:cfcCloneTargetIfIndex,_V:cfcCloneProfileEgressIfType,_W:cfcCloneProfileEgressIf,_X:cfcCloneProfileTableChanged,'cfcFlows':cfcFlows,'cfcFlowIpTable':cfcFlowIpTable,'cfcFlowIpEntry':cfcFlowIpEntry,_H:cfcFlowIndex,_Y:cfcFlowIpStatus,_Z:cfcFlowIpStorageType,_a:cfcFlowIpAddrSrcType,_b:cfcFlowIpAddrSrc,_c:cfcFlowIpAddrDstType,_d:cfcFlowIpAddrDst,_e:cfcFlowIpCreateTime,'cfcFlowStats':cfcFlowStats,'cfcFlowStatsTable':cfcFlowStatsTable,'cfcFlowStatsEntry':cfcFlowStatsEntry,_f:cfcFlowPkts,_g:cfcFlowOctets,'ciscoFlowCloneMIBConformance':ciscoFlowCloneMIBConformance,'ciscoFlowCloneMIBCompliances':ciscoFlowCloneMIBCompliances,'ciscoCloneFlowCompliance01':ciscoCloneFlowCompliance01,'ciscoFlowCloneMIBGroups':ciscoFlowCloneMIBGroups,_h:cfcCloneProfileGroup,_i:cfcFlowGroup,_j:cfcFlowStatsGroup})
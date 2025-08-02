_s='ciscoIpLocalPoolPriorityGroup'
_r='deprecated'
_q='cilpPercentAddrUsedHiNotif'
_p='cilpPercentAddrUsedLoNotif'
_o='ciscoIpLocalPoolInUseAddrNoti'
_n='cIpLocalPoolPriority'
_m='cIpLocalPoolPercentAddrThldHi'
_l='cIpLocalPoolPercentAddrThldLo'
_k='cIpLocalPoolAllocUser'
_j='cIpLocalPoolAllocIfIndex'
_i='cIpLocalPoolStatInUseAddrThldHi'
_h='cIpLocalPoolStatInUseAddrThldLo'
_g='cIpLocalPoolStatHiWaterUsedAddrs'
_f='cIpLocalPoolGroupInUseAddrs'
_e='cIpLocalPoolGroupFreeAddrs'
_d='cIpLocalPoolRowStatus'
_c='cIpLocalPoolGroupContainedIn'
_b='cIpLocalPoolInUseAddrs'
_a='cIpLocalPoolFreeAddrs'
_Z='cIpLocalPoolAddressHi'
_Y='cIpLocalPoolNotificationsEnable'
_X='cIpLocalPoolAllocAddr'
_W='cIpLocalPoolAllocAddrType'
_V='CIpLocalPoolGroupNameOrNull'
_U='cIpLocalPoolAddressLo'
_T='cIpLocalPoolAddrType'
_S='ciscoIpLocalPoolNotifGroupSup1'
_R='ciscoIpLocalPoolStatsGroupSup1'
_Q='ciscoIpLocalPoolNotifGroup'
_P='CIpLocalPoolPercentage'
_O='cIpLocalPoolChildIndex'
_N='cIpLocalPoolGroupName'
_M='ciscoIpLocalPoolGroupGroup'
_L='ciscoIpLocalPoolStatsGroup'
_K='ciscoIpLocalPoolConfigGroup'
_J='read-create'
_I='cIpLocalPoolName'
_H='Unsigned32'
_G='cIpLocalPoolStatInUseAddrs'
_F='cIpLocalPoolStatFreeAddrs'
_E='not-accessible'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-IP-LOCAL-POOL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
ciscoIpLocalPoolMIB=ModuleIdentity((1,3,6,1,4,1,9,9,326))
if mibBuilder.loadTexts:ciscoIpLocalPoolMIB.setRevisions(('2007-11-12 00:00','2005-01-11 00:00','2003-04-03 20:00'))
class CIpLocalPoolName(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
class CIpLocalPoolGroupNameOrNull(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
class CIpLocalPoolPercentage(TextualConvention,Gauge32):status=_B;displayHint='d-2';subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CiscoIpLocalPoolMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIpLocalPoolMIBNotifs=_CiscoIpLocalPoolMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,326,0))
_CiscoIpLocalPoolMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpLocalPoolMIBObjects=_CiscoIpLocalPoolMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,326,1))
_CIpLocalPoolConfig_ObjectIdentity=ObjectIdentity
cIpLocalPoolConfig=_CIpLocalPoolConfig_ObjectIdentity((1,3,6,1,4,1,9,9,326,1,1))
_CIpLocalPoolNotificationsEnable_Type=TruthValue
_CIpLocalPoolNotificationsEnable_Object=MibScalar
cIpLocalPoolNotificationsEnable=_CIpLocalPoolNotificationsEnable_Object((1,3,6,1,4,1,9,9,326,1,1,1),_CIpLocalPoolNotificationsEnable_Type())
cIpLocalPoolNotificationsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpLocalPoolNotificationsEnable.setStatus(_B)
_CIpLocalPoolConfigTable_Object=MibTable
cIpLocalPoolConfigTable=_CIpLocalPoolConfigTable_Object((1,3,6,1,4,1,9,9,326,1,1,2))
if mibBuilder.loadTexts:cIpLocalPoolConfigTable.setStatus(_B)
_CIpLocalPoolConfigEntry_Object=MibTableRow
cIpLocalPoolConfigEntry=_CIpLocalPoolConfigEntry_Object((1,3,6,1,4,1,9,9,326,1,1,2,1))
cIpLocalPoolConfigEntry.setIndexNames((0,_A,_I),(0,_A,_T),(0,_A,_U))
if mibBuilder.loadTexts:cIpLocalPoolConfigEntry.setStatus(_B)
_CIpLocalPoolName_Type=CIpLocalPoolName
_CIpLocalPoolName_Object=MibTableColumn
cIpLocalPoolName=_CIpLocalPoolName_Object((1,3,6,1,4,1,9,9,326,1,1,2,1,1),_CIpLocalPoolName_Type())
cIpLocalPoolName.setMaxAccess(_E)
if mibBuilder.loadTexts:cIpLocalPoolName.setStatus(_B)
_CIpLocalPoolAddrType_Type=InetAddressType
_CIpLocalPoolAddrType_Object=MibTableColumn
cIpLocalPoolAddrType=_CIpLocalPoolAddrType_Object((1,3,6,1,4,1,9,9,326,1,1,2,1,2),_CIpLocalPoolAddrType_Type())
cIpLocalPoolAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:cIpLocalPoolAddrType.setStatus(_B)
_CIpLocalPoolAddressLo_Type=InetAddress
_CIpLocalPoolAddressLo_Object=MibTableColumn
cIpLocalPoolAddressLo=_CIpLocalPoolAddressLo_Object((1,3,6,1,4,1,9,9,326,1,1,2,1,3),_CIpLocalPoolAddressLo_Type())
cIpLocalPoolAddressLo.setMaxAccess(_E)
if mibBuilder.loadTexts:cIpLocalPoolAddressLo.setStatus(_B)
_CIpLocalPoolAddressHi_Type=InetAddress
_CIpLocalPoolAddressHi_Object=MibTableColumn
cIpLocalPoolAddressHi=_CIpLocalPoolAddressHi_Object((1,3,6,1,4,1,9,9,326,1,1,2,1,4),_CIpLocalPoolAddressHi_Type())
cIpLocalPoolAddressHi.setMaxAccess(_J)
if mibBuilder.loadTexts:cIpLocalPoolAddressHi.setStatus(_B)
_CIpLocalPoolFreeAddrs_Type=Gauge32
_CIpLocalPoolFreeAddrs_Object=MibTableColumn
cIpLocalPoolFreeAddrs=_CIpLocalPoolFreeAddrs_Object((1,3,6,1,4,1,9,9,326,1,1,2,1,5),_CIpLocalPoolFreeAddrs_Type())
cIpLocalPoolFreeAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpLocalPoolFreeAddrs.setStatus(_B)
_CIpLocalPoolInUseAddrs_Type=Gauge32
_CIpLocalPoolInUseAddrs_Object=MibTableColumn
cIpLocalPoolInUseAddrs=_CIpLocalPoolInUseAddrs_Object((1,3,6,1,4,1,9,9,326,1,1,2,1,6),_CIpLocalPoolInUseAddrs_Type())
cIpLocalPoolInUseAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpLocalPoolInUseAddrs.setStatus(_B)
class _CIpLocalPoolGroupContainedIn_Type(CIpLocalPoolGroupNameOrNull):defaultValue=OctetString('')
_CIpLocalPoolGroupContainedIn_Type.__name__=_V
_CIpLocalPoolGroupContainedIn_Object=MibTableColumn
cIpLocalPoolGroupContainedIn=_CIpLocalPoolGroupContainedIn_Object((1,3,6,1,4,1,9,9,326,1,1,2,1,7),_CIpLocalPoolGroupContainedIn_Type())
cIpLocalPoolGroupContainedIn.setMaxAccess(_J)
if mibBuilder.loadTexts:cIpLocalPoolGroupContainedIn.setStatus(_B)
_CIpLocalPoolRowStatus_Type=RowStatus
_CIpLocalPoolRowStatus_Object=MibTableColumn
cIpLocalPoolRowStatus=_CIpLocalPoolRowStatus_Object((1,3,6,1,4,1,9,9,326,1,1,2,1,8),_CIpLocalPoolRowStatus_Type())
cIpLocalPoolRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:cIpLocalPoolRowStatus.setStatus(_B)
class _CIpLocalPoolPriority_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CIpLocalPoolPriority_Type.__name__=_H
_CIpLocalPoolPriority_Object=MibTableColumn
cIpLocalPoolPriority=_CIpLocalPoolPriority_Object((1,3,6,1,4,1,9,9,326,1,1,2,1,9),_CIpLocalPoolPriority_Type())
cIpLocalPoolPriority.setMaxAccess(_J)
if mibBuilder.loadTexts:cIpLocalPoolPriority.setStatus(_B)
_CIpLocalPoolGroup_ObjectIdentity=ObjectIdentity
cIpLocalPoolGroup=_CIpLocalPoolGroup_ObjectIdentity((1,3,6,1,4,1,9,9,326,1,2))
_CIpLocalPoolGroupContainsTable_Object=MibTable
cIpLocalPoolGroupContainsTable=_CIpLocalPoolGroupContainsTable_Object((1,3,6,1,4,1,9,9,326,1,2,1))
if mibBuilder.loadTexts:cIpLocalPoolGroupContainsTable.setStatus(_B)
_CIpLocalPoolGroupContainsEntry_Object=MibTableRow
cIpLocalPoolGroupContainsEntry=_CIpLocalPoolGroupContainsEntry_Object((1,3,6,1,4,1,9,9,326,1,2,1,1))
cIpLocalPoolGroupContainsEntry.setIndexNames((0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:cIpLocalPoolGroupContainsEntry.setStatus(_B)
_CIpLocalPoolGroupName_Type=CIpLocalPoolGroupNameOrNull
_CIpLocalPoolGroupName_Object=MibTableColumn
cIpLocalPoolGroupName=_CIpLocalPoolGroupName_Object((1,3,6,1,4,1,9,9,326,1,2,1,1,1),_CIpLocalPoolGroupName_Type())
cIpLocalPoolGroupName.setMaxAccess(_E)
if mibBuilder.loadTexts:cIpLocalPoolGroupName.setStatus(_B)
_CIpLocalPoolChildIndex_Type=CIpLocalPoolName
_CIpLocalPoolChildIndex_Object=MibTableColumn
cIpLocalPoolChildIndex=_CIpLocalPoolChildIndex_Object((1,3,6,1,4,1,9,9,326,1,2,1,1,2),_CIpLocalPoolChildIndex_Type())
cIpLocalPoolChildIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpLocalPoolChildIndex.setStatus(_B)
_CIpLocalPoolGroupTable_Object=MibTable
cIpLocalPoolGroupTable=_CIpLocalPoolGroupTable_Object((1,3,6,1,4,1,9,9,326,1,2,2))
if mibBuilder.loadTexts:cIpLocalPoolGroupTable.setStatus(_B)
_CIpLocalPoolGroupEntry_Object=MibTableRow
cIpLocalPoolGroupEntry=_CIpLocalPoolGroupEntry_Object((1,3,6,1,4,1,9,9,326,1,2,2,1))
cIpLocalPoolGroupEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:cIpLocalPoolGroupEntry.setStatus(_B)
_CIpLocalPoolGroupFreeAddrs_Type=Gauge32
_CIpLocalPoolGroupFreeAddrs_Object=MibTableColumn
cIpLocalPoolGroupFreeAddrs=_CIpLocalPoolGroupFreeAddrs_Object((1,3,6,1,4,1,9,9,326,1,2,2,1,1),_CIpLocalPoolGroupFreeAddrs_Type())
cIpLocalPoolGroupFreeAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpLocalPoolGroupFreeAddrs.setStatus(_B)
_CIpLocalPoolGroupInUseAddrs_Type=Gauge32
_CIpLocalPoolGroupInUseAddrs_Object=MibTableColumn
cIpLocalPoolGroupInUseAddrs=_CIpLocalPoolGroupInUseAddrs_Object((1,3,6,1,4,1,9,9,326,1,2,2,1,2),_CIpLocalPoolGroupInUseAddrs_Type())
cIpLocalPoolGroupInUseAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpLocalPoolGroupInUseAddrs.setStatus(_B)
_CIpLocalPoolStats_ObjectIdentity=ObjectIdentity
cIpLocalPoolStats=_CIpLocalPoolStats_ObjectIdentity((1,3,6,1,4,1,9,9,326,1,3))
_CIpLocalPoolStatsTable_Object=MibTable
cIpLocalPoolStatsTable=_CIpLocalPoolStatsTable_Object((1,3,6,1,4,1,9,9,326,1,3,1))
if mibBuilder.loadTexts:cIpLocalPoolStatsTable.setStatus(_B)
_CIpLocalPoolStatsEntry_Object=MibTableRow
cIpLocalPoolStatsEntry=_CIpLocalPoolStatsEntry_Object((1,3,6,1,4,1,9,9,326,1,3,1,1))
cIpLocalPoolStatsEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:cIpLocalPoolStatsEntry.setStatus(_B)
_CIpLocalPoolStatFreeAddrs_Type=Gauge32
_CIpLocalPoolStatFreeAddrs_Object=MibTableColumn
cIpLocalPoolStatFreeAddrs=_CIpLocalPoolStatFreeAddrs_Object((1,3,6,1,4,1,9,9,326,1,3,1,1,1),_CIpLocalPoolStatFreeAddrs_Type())
cIpLocalPoolStatFreeAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpLocalPoolStatFreeAddrs.setStatus(_B)
_CIpLocalPoolStatInUseAddrs_Type=Gauge32
_CIpLocalPoolStatInUseAddrs_Object=MibTableColumn
cIpLocalPoolStatInUseAddrs=_CIpLocalPoolStatInUseAddrs_Object((1,3,6,1,4,1,9,9,326,1,3,1,1,2),_CIpLocalPoolStatInUseAddrs_Type())
cIpLocalPoolStatInUseAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpLocalPoolStatInUseAddrs.setStatus(_B)
_CIpLocalPoolStatHiWaterUsedAddrs_Type=Unsigned32
_CIpLocalPoolStatHiWaterUsedAddrs_Object=MibTableColumn
cIpLocalPoolStatHiWaterUsedAddrs=_CIpLocalPoolStatHiWaterUsedAddrs_Object((1,3,6,1,4,1,9,9,326,1,3,1,1,3),_CIpLocalPoolStatHiWaterUsedAddrs_Type())
cIpLocalPoolStatHiWaterUsedAddrs.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpLocalPoolStatHiWaterUsedAddrs.setStatus(_B)
class _CIpLocalPoolStatInUseAddrThldLo_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CIpLocalPoolStatInUseAddrThldLo_Type.__name__=_H
_CIpLocalPoolStatInUseAddrThldLo_Object=MibTableColumn
cIpLocalPoolStatInUseAddrThldLo=_CIpLocalPoolStatInUseAddrThldLo_Object((1,3,6,1,4,1,9,9,326,1,3,1,1,4),_CIpLocalPoolStatInUseAddrThldLo_Type())
cIpLocalPoolStatInUseAddrThldLo.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpLocalPoolStatInUseAddrThldLo.setStatus(_B)
class _CIpLocalPoolStatInUseAddrThldHi_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CIpLocalPoolStatInUseAddrThldHi_Type.__name__=_H
_CIpLocalPoolStatInUseAddrThldHi_Object=MibTableColumn
cIpLocalPoolStatInUseAddrThldHi=_CIpLocalPoolStatInUseAddrThldHi_Object((1,3,6,1,4,1,9,9,326,1,3,1,1,5),_CIpLocalPoolStatInUseAddrThldHi_Type())
cIpLocalPoolStatInUseAddrThldHi.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpLocalPoolStatInUseAddrThldHi.setStatus(_B)
class _CIpLocalPoolPercentAddrThldLo_Type(CIpLocalPoolPercentage):defaultValue=0
_CIpLocalPoolPercentAddrThldLo_Type.__name__=_P
_CIpLocalPoolPercentAddrThldLo_Object=MibTableColumn
cIpLocalPoolPercentAddrThldLo=_CIpLocalPoolPercentAddrThldLo_Object((1,3,6,1,4,1,9,9,326,1,3,1,1,6),_CIpLocalPoolPercentAddrThldLo_Type())
cIpLocalPoolPercentAddrThldLo.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpLocalPoolPercentAddrThldLo.setStatus(_B)
class _CIpLocalPoolPercentAddrThldHi_Type(CIpLocalPoolPercentage):defaultValue=100
_CIpLocalPoolPercentAddrThldHi_Type.__name__=_P
_CIpLocalPoolPercentAddrThldHi_Object=MibTableColumn
cIpLocalPoolPercentAddrThldHi=_CIpLocalPoolPercentAddrThldHi_Object((1,3,6,1,4,1,9,9,326,1,3,1,1,7),_CIpLocalPoolPercentAddrThldHi_Type())
cIpLocalPoolPercentAddrThldHi.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpLocalPoolPercentAddrThldHi.setStatus(_B)
_CIpLocalPoolAllocTable_Object=MibTable
cIpLocalPoolAllocTable=_CIpLocalPoolAllocTable_Object((1,3,6,1,4,1,9,9,326,1,3,2))
if mibBuilder.loadTexts:cIpLocalPoolAllocTable.setStatus(_B)
_CIpLocalPoolAllocEntry_Object=MibTableRow
cIpLocalPoolAllocEntry=_CIpLocalPoolAllocEntry_Object((1,3,6,1,4,1,9,9,326,1,3,2,1))
cIpLocalPoolAllocEntry.setIndexNames((0,_A,_I),(0,_A,_W),(0,_A,_X))
if mibBuilder.loadTexts:cIpLocalPoolAllocEntry.setStatus(_B)
_CIpLocalPoolAllocAddrType_Type=InetAddressType
_CIpLocalPoolAllocAddrType_Object=MibTableColumn
cIpLocalPoolAllocAddrType=_CIpLocalPoolAllocAddrType_Object((1,3,6,1,4,1,9,9,326,1,3,2,1,1),_CIpLocalPoolAllocAddrType_Type())
cIpLocalPoolAllocAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:cIpLocalPoolAllocAddrType.setStatus(_B)
_CIpLocalPoolAllocAddr_Type=InetAddress
_CIpLocalPoolAllocAddr_Object=MibTableColumn
cIpLocalPoolAllocAddr=_CIpLocalPoolAllocAddr_Object((1,3,6,1,4,1,9,9,326,1,3,2,1,2),_CIpLocalPoolAllocAddr_Type())
cIpLocalPoolAllocAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cIpLocalPoolAllocAddr.setStatus(_B)
_CIpLocalPoolAllocIfIndex_Type=InterfaceIndexOrZero
_CIpLocalPoolAllocIfIndex_Object=MibTableColumn
cIpLocalPoolAllocIfIndex=_CIpLocalPoolAllocIfIndex_Object((1,3,6,1,4,1,9,9,326,1,3,2,1,3),_CIpLocalPoolAllocIfIndex_Type())
cIpLocalPoolAllocIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpLocalPoolAllocIfIndex.setStatus(_B)
_CIpLocalPoolAllocUser_Type=SnmpAdminString
_CIpLocalPoolAllocUser_Object=MibTableColumn
cIpLocalPoolAllocUser=_CIpLocalPoolAllocUser_Object((1,3,6,1,4,1,9,9,326,1,3,2,1,4),_CIpLocalPoolAllocUser_Type())
cIpLocalPoolAllocUser.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpLocalPoolAllocUser.setStatus(_B)
_CiscoIpLocalPoolMIBConform_ObjectIdentity=ObjectIdentity
ciscoIpLocalPoolMIBConform=_CiscoIpLocalPoolMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,326,2))
_CiscoIpLocalPoolMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIpLocalPoolMIBCompliances=_CiscoIpLocalPoolMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,326,2,1))
_CiscoIpLocalPoolMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpLocalPoolMIBGroups=_CiscoIpLocalPoolMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,326,2,2))
ciscoIpLocalPoolConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,326,2,2,1))
ciscoIpLocalPoolConfigGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:ciscoIpLocalPoolConfigGroup.setStatus(_B)
ciscoIpLocalPoolGroupGroup=ObjectGroup((1,3,6,1,4,1,9,9,326,2,2,2))
ciscoIpLocalPoolGroupGroup.setObjects(*((_A,_O),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:ciscoIpLocalPoolGroupGroup.setStatus(_B)
ciscoIpLocalPoolStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,326,2,2,3))
ciscoIpLocalPoolStatsGroup.setObjects(*((_A,_F),(_A,_G),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:ciscoIpLocalPoolStatsGroup.setStatus(_B)
ciscoIpLocalPoolStatsGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,326,2,2,5))
ciscoIpLocalPoolStatsGroupSup1.setObjects(*((_A,_l),(_A,_m)))
if mibBuilder.loadTexts:ciscoIpLocalPoolStatsGroupSup1.setStatus(_B)
ciscoIpLocalPoolPriorityGroup=ObjectGroup((1,3,6,1,4,1,9,9,326,2,2,7))
ciscoIpLocalPoolPriorityGroup.setObjects((_A,_n))
if mibBuilder.loadTexts:ciscoIpLocalPoolPriorityGroup.setStatus(_B)
ciscoIpLocalPoolInUseAddrNoti=NotificationType((1,3,6,1,4,1,9,9,326,0,1))
ciscoIpLocalPoolInUseAddrNoti.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ciscoIpLocalPoolInUseAddrNoti.setStatus(_B)
cilpPercentAddrUsedLoNotif=NotificationType((1,3,6,1,4,1,9,9,326,0,2))
cilpPercentAddrUsedLoNotif.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cilpPercentAddrUsedLoNotif.setStatus(_B)
cilpPercentAddrUsedHiNotif=NotificationType((1,3,6,1,4,1,9,9,326,0,3))
cilpPercentAddrUsedHiNotif.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cilpPercentAddrUsedHiNotif.setStatus(_B)
ciscoIpLocalPoolNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,326,2,2,4))
ciscoIpLocalPoolNotifGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:ciscoIpLocalPoolNotifGroup.setStatus(_B)
ciscoIpLocalPoolNotifGroupSup1=NotificationGroup((1,3,6,1,4,1,9,9,326,2,2,6))
ciscoIpLocalPoolNotifGroupSup1.setObjects(*((_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ciscoIpLocalPoolNotifGroupSup1.setStatus(_B)
ciscoIpLocalPoolMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,326,2,1,1))
ciscoIpLocalPoolMIBCompliance.setObjects(*((_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ciscoIpLocalPoolMIBCompliance.setStatus(_r)
ciscoIpLocalPoolMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,326,2,1,2))
ciscoIpLocalPoolMIBCompliance1.setObjects(*((_A,_K),(_A,_L),(_A,_Q),(_A,_M),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoIpLocalPoolMIBCompliance1.setStatus(_r)
ciscoIpLocalPoolMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,326,2,1,3))
ciscoIpLocalPoolMIBCompliance2.setObjects(*((_A,_K),(_A,_L),(_A,_Q),(_A,_s),(_A,_M),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoIpLocalPoolMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CIpLocalPoolName':CIpLocalPoolName,_V:CIpLocalPoolGroupNameOrNull,_P:CIpLocalPoolPercentage,'ciscoIpLocalPoolMIB':ciscoIpLocalPoolMIB,'ciscoIpLocalPoolMIBNotifs':ciscoIpLocalPoolMIBNotifs,_o:ciscoIpLocalPoolInUseAddrNoti,_p:cilpPercentAddrUsedLoNotif,_q:cilpPercentAddrUsedHiNotif,'ciscoIpLocalPoolMIBObjects':ciscoIpLocalPoolMIBObjects,'cIpLocalPoolConfig':cIpLocalPoolConfig,_Y:cIpLocalPoolNotificationsEnable,'cIpLocalPoolConfigTable':cIpLocalPoolConfigTable,'cIpLocalPoolConfigEntry':cIpLocalPoolConfigEntry,_I:cIpLocalPoolName,_T:cIpLocalPoolAddrType,_U:cIpLocalPoolAddressLo,_Z:cIpLocalPoolAddressHi,_a:cIpLocalPoolFreeAddrs,_b:cIpLocalPoolInUseAddrs,_c:cIpLocalPoolGroupContainedIn,_d:cIpLocalPoolRowStatus,_n:cIpLocalPoolPriority,'cIpLocalPoolGroup':cIpLocalPoolGroup,'cIpLocalPoolGroupContainsTable':cIpLocalPoolGroupContainsTable,'cIpLocalPoolGroupContainsEntry':cIpLocalPoolGroupContainsEntry,_N:cIpLocalPoolGroupName,_O:cIpLocalPoolChildIndex,'cIpLocalPoolGroupTable':cIpLocalPoolGroupTable,'cIpLocalPoolGroupEntry':cIpLocalPoolGroupEntry,_e:cIpLocalPoolGroupFreeAddrs,_f:cIpLocalPoolGroupInUseAddrs,'cIpLocalPoolStats':cIpLocalPoolStats,'cIpLocalPoolStatsTable':cIpLocalPoolStatsTable,'cIpLocalPoolStatsEntry':cIpLocalPoolStatsEntry,_F:cIpLocalPoolStatFreeAddrs,_G:cIpLocalPoolStatInUseAddrs,_g:cIpLocalPoolStatHiWaterUsedAddrs,_h:cIpLocalPoolStatInUseAddrThldLo,_i:cIpLocalPoolStatInUseAddrThldHi,_l:cIpLocalPoolPercentAddrThldLo,_m:cIpLocalPoolPercentAddrThldHi,'cIpLocalPoolAllocTable':cIpLocalPoolAllocTable,'cIpLocalPoolAllocEntry':cIpLocalPoolAllocEntry,_W:cIpLocalPoolAllocAddrType,_X:cIpLocalPoolAllocAddr,_j:cIpLocalPoolAllocIfIndex,_k:cIpLocalPoolAllocUser,'ciscoIpLocalPoolMIBConform':ciscoIpLocalPoolMIBConform,'ciscoIpLocalPoolMIBCompliances':ciscoIpLocalPoolMIBCompliances,'ciscoIpLocalPoolMIBCompliance':ciscoIpLocalPoolMIBCompliance,'ciscoIpLocalPoolMIBCompliance1':ciscoIpLocalPoolMIBCompliance1,'ciscoIpLocalPoolMIBCompliance2':ciscoIpLocalPoolMIBCompliance2,'ciscoIpLocalPoolMIBGroups':ciscoIpLocalPoolMIBGroups,_K:ciscoIpLocalPoolConfigGroup,_M:ciscoIpLocalPoolGroupGroup,_L:ciscoIpLocalPoolStatsGroup,_Q:ciscoIpLocalPoolNotifGroup,_R:ciscoIpLocalPoolStatsGroupSup1,_S:ciscoIpLocalPoolNotifGroupSup1,_s:ciscoIpLocalPoolPriorityGroup})
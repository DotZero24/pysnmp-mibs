_V='lldpStatsGroup'
_U='lldpConfigGroup'
_T='lldpStatsOutPkts'
_S='lldpStatsInErrors'
_R='lldpStatsInGoodPkts'
_Q='lldpMessageTxHoldTime'
_P='lldpMessageTxInterval'
_O='lldpOperStatus'
_N='lldpAdminStatus'
_M='lldpRcvDeviceID'
_L='lldpRcvIfIndex'
_K='lldpStatsPortIfIndex'
_J='lldpSuppressPortIfIndex'
_I='seconds'
_H='not-accessible'
_G='EnabledStatus'
_F='DisplayString'
_E='Integer32'
_D='read-write'
_C='FS-LLDP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','TextualConvention')
fsLldpMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,32))
if mibBuilder.loadTexts:fsLldpMIB.setRevisions(('2003-04-01 00:00',))
_LldpMibObjects_ObjectIdentity=ObjectIdentity
lldpMibObjects=_LldpMibObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,32,1))
_LldpConfig_ObjectIdentity=ObjectIdentity
lldpConfig=_LldpConfig_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,32,1,1))
class _LldpAdminStatus_Type(EnabledStatus):defaultValue=1
_LldpAdminStatus_Type.__name__=_G
_LldpAdminStatus_Object=MibScalar
lldpAdminStatus=_LldpAdminStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,1,1),_LldpAdminStatus_Type())
lldpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpAdminStatus.setStatus(_A)
_LldpOperStatus_Type=EnabledStatus
_LldpOperStatus_Object=MibScalar
lldpOperStatus=_LldpOperStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,1,2),_LldpOperStatus_Type())
lldpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpOperStatus.setStatus(_A)
class _LldpMessageTxInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,299))
_LldpMessageTxInterval_Type.__name__=_E
_LldpMessageTxInterval_Object=MibScalar
lldpMessageTxInterval=_LldpMessageTxInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,1,3),_LldpMessageTxInterval_Type())
lldpMessageTxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMessageTxInterval.setStatus(_A)
if mibBuilder.loadTexts:lldpMessageTxInterval.setUnits(_I)
class _LldpMessageTxHoldTime_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_LldpMessageTxHoldTime_Type.__name__=_E
_LldpMessageTxHoldTime_Object=MibScalar
lldpMessageTxHoldTime=_LldpMessageTxHoldTime_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,1,4),_LldpMessageTxHoldTime_Type())
lldpMessageTxHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMessageTxHoldTime.setStatus(_A)
if mibBuilder.loadTexts:lldpMessageTxHoldTime.setUnits(_I)
_LldpDeviceID_Type=MacAddress
_LldpDeviceID_Object=MibScalar
lldpDeviceID=_LldpDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,1,5),_LldpDeviceID_Type())
lldpDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpDeviceID.setStatus(_A)
_LldpSuppressTable_Object=MibTable
lldpSuppressTable=_LldpSuppressTable_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,1,6))
if mibBuilder.loadTexts:lldpSuppressTable.setStatus(_A)
_LldpSuppressEntry_Object=MibTableRow
lldpSuppressEntry=_LldpSuppressEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,1,6,1))
lldpSuppressEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:lldpSuppressEntry.setStatus(_A)
_LldpSuppressPortIfIndex_Type=IfIndex
_LldpSuppressPortIfIndex_Object=MibTableColumn
lldpSuppressPortIfIndex=_LldpSuppressPortIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,1,6,1,1),_LldpSuppressPortIfIndex_Type())
lldpSuppressPortIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lldpSuppressPortIfIndex.setStatus(_A)
class _LldpSuppressPortStatus_Type(EnabledStatus):defaultValue=1
_LldpSuppressPortStatus_Type.__name__=_G
_LldpSuppressPortStatus_Object=MibTableColumn
lldpSuppressPortStatus=_LldpSuppressPortStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,1,6,1,2),_LldpSuppressPortStatus_Type())
lldpSuppressPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpSuppressPortStatus.setStatus(_A)
_LldpStats_ObjectIdentity=ObjectIdentity
lldpStats=_LldpStats_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,32,1,2))
_LldpStatsTable_Object=MibTable
lldpStatsTable=_LldpStatsTable_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,2,1))
if mibBuilder.loadTexts:lldpStatsTable.setStatus(_A)
_LldpStatsEntry_Object=MibTableRow
lldpStatsEntry=_LldpStatsEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,2,1,1))
lldpStatsEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:lldpStatsEntry.setStatus(_A)
_LldpStatsPortIfIndex_Type=IfIndex
_LldpStatsPortIfIndex_Object=MibTableColumn
lldpStatsPortIfIndex=_LldpStatsPortIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,2,1,1,1),_LldpStatsPortIfIndex_Type())
lldpStatsPortIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lldpStatsPortIfIndex.setStatus(_A)
_LldpStatsInGoodPkts_Type=Counter32
_LldpStatsInGoodPkts_Object=MibTableColumn
lldpStatsInGoodPkts=_LldpStatsInGoodPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,2,1,1,2),_LldpStatsInGoodPkts_Type())
lldpStatsInGoodPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpStatsInGoodPkts.setStatus(_A)
_LldpStatsInErrors_Type=Counter32
_LldpStatsInErrors_Object=MibTableColumn
lldpStatsInErrors=_LldpStatsInErrors_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,2,1,1,3),_LldpStatsInErrors_Type())
lldpStatsInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpStatsInErrors.setStatus(_A)
_LldpStatsOutPkts_Type=Counter32
_LldpStatsOutPkts_Object=MibTableColumn
lldpStatsOutPkts=_LldpStatsOutPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,2,1,1,4),_LldpStatsOutPkts_Type())
lldpStatsOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpStatsOutPkts.setStatus(_A)
_LldpStatsClear_Type=Integer32
_LldpStatsClear_Object=MibTableColumn
lldpStatsClear=_LldpStatsClear_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,2,1,1,5),_LldpStatsClear_Type())
lldpStatsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpStatsClear.setStatus(_A)
_LldpRcvObjects_ObjectIdentity=ObjectIdentity
lldpRcvObjects=_LldpRcvObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,32,1,3))
_LldpRcvTable_Object=MibTable
lldpRcvTable=_LldpRcvTable_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,3,1))
if mibBuilder.loadTexts:lldpRcvTable.setStatus(_A)
_LldpRcvEntry_Object=MibTableRow
lldpRcvEntry=_LldpRcvEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,3,1,1))
lldpRcvEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:lldpRcvEntry.setStatus(_A)
_LldpRcvIfIndex_Type=IfIndex
_LldpRcvIfIndex_Object=MibTableColumn
lldpRcvIfIndex=_LldpRcvIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,3,1,1,1),_LldpRcvIfIndex_Type())
lldpRcvIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lldpRcvIfIndex.setStatus(_A)
_LldpRcvDeviceID_Type=MacAddress
_LldpRcvDeviceID_Object=MibTableColumn
lldpRcvDeviceID=_LldpRcvDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,3,1,1,2),_LldpRcvDeviceID_Type())
lldpRcvDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpRcvDeviceID.setStatus(_A)
_LldpRcvMgmtAddress_Type=MacAddress
_LldpRcvMgmtAddress_Object=MibTableColumn
lldpRcvMgmtAddress=_LldpRcvMgmtAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,3,1,1,3),_LldpRcvMgmtAddress_Type())
lldpRcvMgmtAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpRcvMgmtAddress.setStatus(_A)
_LldpRcvPortIDSubtype_Type=Integer32
_LldpRcvPortIDSubtype_Object=MibTableColumn
lldpRcvPortIDSubtype=_LldpRcvPortIDSubtype_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,3,1,1,4),_LldpRcvPortIDSubtype_Type())
lldpRcvPortIDSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpRcvPortIDSubtype.setStatus(_A)
class _LldpRcvPortInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpRcvPortInfo_Type.__name__=_F
_LldpRcvPortInfo_Object=MibTableColumn
lldpRcvPortInfo=_LldpRcvPortInfo_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,3,1,1,5),_LldpRcvPortInfo_Type())
lldpRcvPortInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpRcvPortInfo.setStatus(_A)
class _LldpRcvClusterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('commandDevice',1),('memberDevice',2),('none',3)))
_LldpRcvClusterMode_Type.__name__=_E
_LldpRcvClusterMode_Object=MibTableColumn
lldpRcvClusterMode=_LldpRcvClusterMode_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,3,1,1,6),_LldpRcvClusterMode_Type())
lldpRcvClusterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpRcvClusterMode.setStatus(_A)
_LldpRcvClusterStatus_Type=EnabledStatus
_LldpRcvClusterStatus_Object=MibTableColumn
lldpRcvClusterStatus=_LldpRcvClusterStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,3,1,1,7),_LldpRcvClusterStatus_Type())
lldpRcvClusterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpRcvClusterStatus.setStatus(_A)
class _LldpRcvClusterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_LldpRcvClusterName_Type.__name__=_F
_LldpRcvClusterName_Object=MibTableColumn
lldpRcvClusterName=_LldpRcvClusterName_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,3,1,1,8),_LldpRcvClusterName_Type())
lldpRcvClusterName.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpRcvClusterName.setStatus(_A)
class _LldpRcvHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_LldpRcvHostName_Type.__name__=_F
_LldpRcvHostName_Object=MibTableColumn
lldpRcvHostName=_LldpRcvHostName_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,3,1,1,9),_LldpRcvHostName_Type())
lldpRcvHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpRcvHostName.setStatus(_A)
_LldpRcvCommandAddress_Type=MacAddress
_LldpRcvCommandAddress_Object=MibTableColumn
lldpRcvCommandAddress=_LldpRcvCommandAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,3,1,1,10),_LldpRcvCommandAddress_Type())
lldpRcvCommandAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpRcvCommandAddress.setStatus(_A)
_LldpRcvTableClear_Type=Integer32
_LldpRcvTableClear_Object=MibScalar
lldpRcvTableClear=_LldpRcvTableClear_Object((1,3,6,1,4,1,52642,1,1,10,2,32,1,3,2),_LldpRcvTableClear_Type())
lldpRcvTableClear.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpRcvTableClear.setStatus(_A)
_LldpMIBConformance_ObjectIdentity=ObjectIdentity
lldpMIBConformance=_LldpMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,32,2))
_LldpMIBCompliances_ObjectIdentity=ObjectIdentity
lldpMIBCompliances=_LldpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,32,2,1))
_LldpMIBGroups_ObjectIdentity=ObjectIdentity
lldpMIBGroups=_LldpMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,32,2,2))
lldpConfigGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,32,2,2,1))
lldpConfigGroup.setObjects(*((_C,_N),(_C,_O),(_C,_P),(_C,_Q)))
if mibBuilder.loadTexts:lldpConfigGroup.setStatus(_A)
lldpStatsGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,32,2,2,2))
lldpStatsGroup.setObjects(*((_C,_R),(_C,_S),(_C,_T)))
if mibBuilder.loadTexts:lldpStatsGroup.setStatus(_A)
lldpCompliances=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,32,2,1,1))
lldpCompliances.setObjects(*((_C,_U),(_C,_V)))
if mibBuilder.loadTexts:lldpCompliances.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsLldpMIB':fsLldpMIB,'lldpMibObjects':lldpMibObjects,'lldpConfig':lldpConfig,_N:lldpAdminStatus,_O:lldpOperStatus,_P:lldpMessageTxInterval,_Q:lldpMessageTxHoldTime,'lldpDeviceID':lldpDeviceID,'lldpSuppressTable':lldpSuppressTable,'lldpSuppressEntry':lldpSuppressEntry,_J:lldpSuppressPortIfIndex,'lldpSuppressPortStatus':lldpSuppressPortStatus,'lldpStats':lldpStats,'lldpStatsTable':lldpStatsTable,'lldpStatsEntry':lldpStatsEntry,_K:lldpStatsPortIfIndex,_R:lldpStatsInGoodPkts,_S:lldpStatsInErrors,_T:lldpStatsOutPkts,'lldpStatsClear':lldpStatsClear,'lldpRcvObjects':lldpRcvObjects,'lldpRcvTable':lldpRcvTable,'lldpRcvEntry':lldpRcvEntry,_L:lldpRcvIfIndex,_M:lldpRcvDeviceID,'lldpRcvMgmtAddress':lldpRcvMgmtAddress,'lldpRcvPortIDSubtype':lldpRcvPortIDSubtype,'lldpRcvPortInfo':lldpRcvPortInfo,'lldpRcvClusterMode':lldpRcvClusterMode,'lldpRcvClusterStatus':lldpRcvClusterStatus,'lldpRcvClusterName':lldpRcvClusterName,'lldpRcvHostName':lldpRcvHostName,'lldpRcvCommandAddress':lldpRcvCommandAddress,'lldpRcvTableClear':lldpRcvTableClear,'lldpMIBConformance':lldpMIBConformance,'lldpMIBCompliances':lldpMIBCompliances,'lldpCompliances':lldpCompliances,'lldpMIBGroups':lldpMIBGroups,_U:lldpConfigGroup,_V:lldpStatsGroup})
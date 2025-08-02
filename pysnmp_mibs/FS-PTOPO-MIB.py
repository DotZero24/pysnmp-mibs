_X='fsptopoMIBGroup'
_W='ptopoConfigHopCount'
_V='ptopoConfigMaxHoldTime'
_U='ptopoConfigInterval'
_T='ptopoDevLastVerifyTime'
_S='ptopoDevHopsToCs'
_R='ptopoDevCSMac'
_Q='ptopoDevClusName'
_P='ptopoDevClusMode'
_O='ptopoDevClusStatus'
_N='ptopoDevHostname'
_M='ptopoConnIsUpStream'
_L='ptopoConnRemotePort'
_K='ptopoConnRemoteDevice'
_J='seconds'
_I='ptopoDevID'
_H='ptopoConnIndex'
_G='read-write'
_F='not-accessible'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='FS-PTOPO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','TextualConvention','TimeStamp')
fsPotopoMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,33))
if mibBuilder.loadTexts:fsPotopoMIB.setRevisions(('2003-04-28 00:00',))
_PtopoMIBObjects_ObjectIdentity=ObjectIdentity
ptopoMIBObjects=_PtopoMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,33,1))
_PtopoConnData_ObjectIdentity=ObjectIdentity
ptopoConnData=_PtopoConnData_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,33,1,1))
_PtopoConnTable_Object=MibTable
ptopoConnTable=_PtopoConnTable_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,1,1))
if mibBuilder.loadTexts:ptopoConnTable.setStatus(_A)
_PtopoConnEntry_Object=MibTableRow
ptopoConnEntry=_PtopoConnEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,1,1,1))
ptopoConnEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:ptopoConnEntry.setStatus(_A)
class _PtopoConnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PtopoConnIndex_Type.__name__=_D
_PtopoConnIndex_Object=MibTableColumn
ptopoConnIndex=_PtopoConnIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,1,1,1,1),_PtopoConnIndex_Type())
ptopoConnIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ptopoConnIndex.setStatus(_A)
_PtopoConnLocalDevice_Type=MacAddress
_PtopoConnLocalDevice_Object=MibTableColumn
ptopoConnLocalDevice=_PtopoConnLocalDevice_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,1,1,1,2),_PtopoConnLocalDevice_Type())
ptopoConnLocalDevice.setMaxAccess(_F)
if mibBuilder.loadTexts:ptopoConnLocalDevice.setStatus(_A)
class _PtopoConnLocalPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PtopoConnLocalPort_Type.__name__=_E
_PtopoConnLocalPort_Object=MibTableColumn
ptopoConnLocalPort=_PtopoConnLocalPort_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,1,1,1,3),_PtopoConnLocalPort_Type())
ptopoConnLocalPort.setMaxAccess(_F)
if mibBuilder.loadTexts:ptopoConnLocalPort.setStatus(_A)
_PtopoConnRemoteDevice_Type=MacAddress
_PtopoConnRemoteDevice_Object=MibTableColumn
ptopoConnRemoteDevice=_PtopoConnRemoteDevice_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,1,1,1,4),_PtopoConnRemoteDevice_Type())
ptopoConnRemoteDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoConnRemoteDevice.setStatus(_A)
class _PtopoConnRemotePort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PtopoConnRemotePort_Type.__name__=_E
_PtopoConnRemotePort_Object=MibTableColumn
ptopoConnRemotePort=_PtopoConnRemotePort_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,1,1,1,5),_PtopoConnRemotePort_Type())
ptopoConnRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoConnRemotePort.setStatus(_A)
class _PtopoConnIsUpStream_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upstream',1),('nonupstream',2)))
_PtopoConnIsUpStream_Type.__name__=_D
_PtopoConnIsUpStream_Object=MibTableColumn
ptopoConnIsUpStream=_PtopoConnIsUpStream_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,1,1,1,6),_PtopoConnIsUpStream_Type())
ptopoConnIsUpStream.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoConnIsUpStream.setStatus(_A)
_PtopoDevData_ObjectIdentity=ObjectIdentity
ptopoDevData=_PtopoDevData_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,33,1,2))
_PtopoDevTable_Object=MibTable
ptopoDevTable=_PtopoDevTable_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,2,1))
if mibBuilder.loadTexts:ptopoDevTable.setStatus(_A)
_PtopoDevEntry_Object=MibTableRow
ptopoDevEntry=_PtopoDevEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,2,1,1))
ptopoDevEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ptopoDevEntry.setStatus(_A)
_PtopoDevID_Type=MacAddress
_PtopoDevID_Object=MibTableColumn
ptopoDevID=_PtopoDevID_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,2,1,1,1),_PtopoDevID_Type())
ptopoDevID.setMaxAccess(_F)
if mibBuilder.loadTexts:ptopoDevID.setStatus(_A)
class _PtopoDevHostname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_PtopoDevHostname_Type.__name__=_E
_PtopoDevHostname_Object=MibTableColumn
ptopoDevHostname=_PtopoDevHostname_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,2,1,1,2),_PtopoDevHostname_Type())
ptopoDevHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoDevHostname.setStatus(_A)
_PtopoDevClusStatus_Type=EnabledStatus
_PtopoDevClusStatus_Object=MibTableColumn
ptopoDevClusStatus=_PtopoDevClusStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,2,1,1,3),_PtopoDevClusStatus_Type())
ptopoDevClusStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoDevClusStatus.setStatus(_A)
class _PtopoDevClusMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('commandDevice',1),('memberDevice',2),('none',3)))
_PtopoDevClusMode_Type.__name__=_D
_PtopoDevClusMode_Object=MibTableColumn
ptopoDevClusMode=_PtopoDevClusMode_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,2,1,1,4),_PtopoDevClusMode_Type())
ptopoDevClusMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoDevClusMode.setStatus(_A)
class _PtopoDevClusName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PtopoDevClusName_Type.__name__=_E
_PtopoDevClusName_Object=MibTableColumn
ptopoDevClusName=_PtopoDevClusName_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,2,1,1,5),_PtopoDevClusName_Type())
ptopoDevClusName.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoDevClusName.setStatus(_A)
_PtopoDevCSMac_Type=MacAddress
_PtopoDevCSMac_Object=MibTableColumn
ptopoDevCSMac=_PtopoDevCSMac_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,2,1,1,6),_PtopoDevCSMac_Type())
ptopoDevCSMac.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoDevCSMac.setStatus(_A)
class _PtopoDevHopsToCs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_PtopoDevHopsToCs_Type.__name__=_D
_PtopoDevHopsToCs_Object=MibTableColumn
ptopoDevHopsToCs=_PtopoDevHopsToCs_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,2,1,1,7),_PtopoDevHopsToCs_Type())
ptopoDevHopsToCs.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoDevHopsToCs.setStatus(_A)
_PtopoDevLastVerifyTime_Type=TimeStamp
_PtopoDevLastVerifyTime_Object=MibTableColumn
ptopoDevLastVerifyTime=_PtopoDevLastVerifyTime_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,2,1,1,8),_PtopoDevLastVerifyTime_Type())
ptopoDevLastVerifyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoDevLastVerifyTime.setStatus(_A)
_PtopoConfig_ObjectIdentity=ObjectIdentity
ptopoConfig=_PtopoConfig_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,33,1,3))
class _PtopoConfigInterval_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_PtopoConfigInterval_Type.__name__=_D
_PtopoConfigInterval_Object=MibScalar
ptopoConfigInterval=_PtopoConfigInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,3,1),_PtopoConfigInterval_Type())
ptopoConfigInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:ptopoConfigInterval.setStatus(_A)
if mibBuilder.loadTexts:ptopoConfigInterval.setUnits(_J)
class _PtopoConfigMaxHoldTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_PtopoConfigMaxHoldTime_Type.__name__=_D
_PtopoConfigMaxHoldTime_Object=MibScalar
ptopoConfigMaxHoldTime=_PtopoConfigMaxHoldTime_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,3,2),_PtopoConfigMaxHoldTime_Type())
ptopoConfigMaxHoldTime.setMaxAccess(_G)
if mibBuilder.loadTexts:ptopoConfigMaxHoldTime.setStatus(_A)
if mibBuilder.loadTexts:ptopoConfigMaxHoldTime.setUnits(_J)
class _PtopoConfigHopCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_PtopoConfigHopCount_Type.__name__=_D
_PtopoConfigHopCount_Object=MibScalar
ptopoConfigHopCount=_PtopoConfigHopCount_Object((1,3,6,1,4,1,52642,1,1,10,2,33,1,3,3),_PtopoConfigHopCount_Type())
ptopoConfigHopCount.setMaxAccess(_G)
if mibBuilder.loadTexts:ptopoConfigHopCount.setStatus(_A)
_FsptopoMIBConformance_ObjectIdentity=ObjectIdentity
fsptopoMIBConformance=_FsptopoMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,33,2))
_FsptopoMIBCompliances_ObjectIdentity=ObjectIdentity
fsptopoMIBCompliances=_FsptopoMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,33,2,1))
_FsptopoMIBGroups_ObjectIdentity=ObjectIdentity
fsptopoMIBGroups=_FsptopoMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,33,2,2))
fsptopoMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,33,2,2,1))
fsptopoMIBGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:fsptopoMIBGroup.setStatus(_A)
fsptopoMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,33,2,1,1))
fsptopoMIBCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:fsptopoMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsPotopoMIB':fsPotopoMIB,'ptopoMIBObjects':ptopoMIBObjects,'ptopoConnData':ptopoConnData,'ptopoConnTable':ptopoConnTable,'ptopoConnEntry':ptopoConnEntry,_H:ptopoConnIndex,'ptopoConnLocalDevice':ptopoConnLocalDevice,'ptopoConnLocalPort':ptopoConnLocalPort,_K:ptopoConnRemoteDevice,_L:ptopoConnRemotePort,_M:ptopoConnIsUpStream,'ptopoDevData':ptopoDevData,'ptopoDevTable':ptopoDevTable,'ptopoDevEntry':ptopoDevEntry,_I:ptopoDevID,_N:ptopoDevHostname,_O:ptopoDevClusStatus,_P:ptopoDevClusMode,_Q:ptopoDevClusName,_R:ptopoDevCSMac,_S:ptopoDevHopsToCs,_T:ptopoDevLastVerifyTime,'ptopoConfig':ptopoConfig,_U:ptopoConfigInterval,_V:ptopoConfigMaxHoldTime,_W:ptopoConfigHopCount,'fsptopoMIBConformance':fsptopoMIBConformance,'fsptopoMIBCompliances':fsptopoMIBCompliances,'fsptopoMIBCompliance':fsptopoMIBCompliance,'fsptopoMIBGroups':fsptopoMIBGroups,_X:fsptopoMIBGroup})
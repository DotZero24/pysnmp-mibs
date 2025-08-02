_J='seconds'
_I='ptopoDevID'
_H='ptopoConnIndex'
_G='read-write'
_F='MY-PTOPO-MIB'
_E='not-accessible'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('MY-TC','ConfigStatus','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
myPotopoMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,33))
if mibBuilder.loadTexts:myPotopoMIB.setRevisions(('2003-04-28 00:00',))
_PtopoMIBObjects_ObjectIdentity=ObjectIdentity
ptopoMIBObjects=_PtopoMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,33,1))
_PtopoConnData_ObjectIdentity=ObjectIdentity
ptopoConnData=_PtopoConnData_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,33,1,1))
_PtopoConnTable_Object=MibTable
ptopoConnTable=_PtopoConnTable_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,1,1))
if mibBuilder.loadTexts:ptopoConnTable.setStatus(_A)
_PtopoConnEntry_Object=MibTableRow
ptopoConnEntry=_PtopoConnEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,1,1,1))
ptopoConnEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:ptopoConnEntry.setStatus(_A)
class _PtopoConnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PtopoConnIndex_Type.__name__=_C
_PtopoConnIndex_Object=MibTableColumn
ptopoConnIndex=_PtopoConnIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,1,1,1,1),_PtopoConnIndex_Type())
ptopoConnIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ptopoConnIndex.setStatus(_A)
_PtopoConnLocalDevice_Type=MacAddress
_PtopoConnLocalDevice_Object=MibTableColumn
ptopoConnLocalDevice=_PtopoConnLocalDevice_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,1,1,1,2),_PtopoConnLocalDevice_Type())
ptopoConnLocalDevice.setMaxAccess(_E)
if mibBuilder.loadTexts:ptopoConnLocalDevice.setStatus(_A)
class _PtopoConnLocalPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PtopoConnLocalPort_Type.__name__=_D
_PtopoConnLocalPort_Object=MibTableColumn
ptopoConnLocalPort=_PtopoConnLocalPort_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,1,1,1,3),_PtopoConnLocalPort_Type())
ptopoConnLocalPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ptopoConnLocalPort.setStatus(_A)
_PtopoConnRemoteDevice_Type=MacAddress
_PtopoConnRemoteDevice_Object=MibTableColumn
ptopoConnRemoteDevice=_PtopoConnRemoteDevice_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,1,1,1,4),_PtopoConnRemoteDevice_Type())
ptopoConnRemoteDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:ptopoConnRemoteDevice.setStatus(_A)
class _PtopoConnRemotePort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PtopoConnRemotePort_Type.__name__=_D
_PtopoConnRemotePort_Object=MibTableColumn
ptopoConnRemotePort=_PtopoConnRemotePort_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,1,1,1,5),_PtopoConnRemotePort_Type())
ptopoConnRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:ptopoConnRemotePort.setStatus(_A)
class _PtopoConnIsUpStream_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upstream',1),('nonupstream',2)))
_PtopoConnIsUpStream_Type.__name__=_C
_PtopoConnIsUpStream_Object=MibTableColumn
ptopoConnIsUpStream=_PtopoConnIsUpStream_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,1,1,1,6),_PtopoConnIsUpStream_Type())
ptopoConnIsUpStream.setMaxAccess(_B)
if mibBuilder.loadTexts:ptopoConnIsUpStream.setStatus(_A)
_PtopoDevData_ObjectIdentity=ObjectIdentity
ptopoDevData=_PtopoDevData_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,33,1,2))
_PtopoDevTable_Object=MibTable
ptopoDevTable=_PtopoDevTable_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,2,1))
if mibBuilder.loadTexts:ptopoDevTable.setStatus(_A)
_PtopoDevEntry_Object=MibTableRow
ptopoDevEntry=_PtopoDevEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,2,1,1))
ptopoDevEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:ptopoDevEntry.setStatus(_A)
_PtopoDevID_Type=MacAddress
_PtopoDevID_Object=MibTableColumn
ptopoDevID=_PtopoDevID_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,2,1,1,1),_PtopoDevID_Type())
ptopoDevID.setMaxAccess(_E)
if mibBuilder.loadTexts:ptopoDevID.setStatus(_A)
class _PtopoDevHostname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_PtopoDevHostname_Type.__name__=_D
_PtopoDevHostname_Object=MibTableColumn
ptopoDevHostname=_PtopoDevHostname_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,2,1,1,2),_PtopoDevHostname_Type())
ptopoDevHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:ptopoDevHostname.setStatus(_A)
_PtopoDevClusStatus_Type=EnabledStatus
_PtopoDevClusStatus_Object=MibTableColumn
ptopoDevClusStatus=_PtopoDevClusStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,2,1,1,3),_PtopoDevClusStatus_Type())
ptopoDevClusStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ptopoDevClusStatus.setStatus(_A)
class _PtopoDevClusMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('commandDevice',1),('memberDevice',2),('none',3)))
_PtopoDevClusMode_Type.__name__=_C
_PtopoDevClusMode_Object=MibTableColumn
ptopoDevClusMode=_PtopoDevClusMode_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,2,1,1,4),_PtopoDevClusMode_Type())
ptopoDevClusMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ptopoDevClusMode.setStatus(_A)
class _PtopoDevClusName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PtopoDevClusName_Type.__name__=_D
_PtopoDevClusName_Object=MibTableColumn
ptopoDevClusName=_PtopoDevClusName_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,2,1,1,5),_PtopoDevClusName_Type())
ptopoDevClusName.setMaxAccess(_B)
if mibBuilder.loadTexts:ptopoDevClusName.setStatus(_A)
_PtopoDevCSMac_Type=MacAddress
_PtopoDevCSMac_Object=MibTableColumn
ptopoDevCSMac=_PtopoDevCSMac_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,2,1,1,6),_PtopoDevCSMac_Type())
ptopoDevCSMac.setMaxAccess(_B)
if mibBuilder.loadTexts:ptopoDevCSMac.setStatus(_A)
class _PtopoDevHopsToCs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_PtopoDevHopsToCs_Type.__name__=_C
_PtopoDevHopsToCs_Object=MibTableColumn
ptopoDevHopsToCs=_PtopoDevHopsToCs_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,2,1,1,7),_PtopoDevHopsToCs_Type())
ptopoDevHopsToCs.setMaxAccess(_B)
if mibBuilder.loadTexts:ptopoDevHopsToCs.setStatus(_A)
_PtopoDevLastVerifyTime_Type=TimeStamp
_PtopoDevLastVerifyTime_Object=MibTableColumn
ptopoDevLastVerifyTime=_PtopoDevLastVerifyTime_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,2,1,1,8),_PtopoDevLastVerifyTime_Type())
ptopoDevLastVerifyTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ptopoDevLastVerifyTime.setStatus(_A)
_PtopoConfig_ObjectIdentity=ObjectIdentity
ptopoConfig=_PtopoConfig_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,33,1,3))
class _PtopoConfigInterval_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_PtopoConfigInterval_Type.__name__=_C
_PtopoConfigInterval_Object=MibScalar
ptopoConfigInterval=_PtopoConfigInterval_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,3,1),_PtopoConfigInterval_Type())
ptopoConfigInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:ptopoConfigInterval.setStatus(_A)
if mibBuilder.loadTexts:ptopoConfigInterval.setUnits(_J)
class _PtopoConfigMaxHoldTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_PtopoConfigMaxHoldTime_Type.__name__=_C
_PtopoConfigMaxHoldTime_Object=MibScalar
ptopoConfigMaxHoldTime=_PtopoConfigMaxHoldTime_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,3,2),_PtopoConfigMaxHoldTime_Type())
ptopoConfigMaxHoldTime.setMaxAccess(_G)
if mibBuilder.loadTexts:ptopoConfigMaxHoldTime.setStatus(_A)
if mibBuilder.loadTexts:ptopoConfigMaxHoldTime.setUnits(_J)
class _PtopoConfigHopCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_PtopoConfigHopCount_Type.__name__=_C
_PtopoConfigHopCount_Object=MibScalar
ptopoConfigHopCount=_PtopoConfigHopCount_Object((1,3,6,1,4,1,4881,1,1,10,2,33,1,3,3),_PtopoConfigHopCount_Type())
ptopoConfigHopCount.setMaxAccess(_G)
if mibBuilder.loadTexts:ptopoConfigHopCount.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'myPotopoMIB':myPotopoMIB,'ptopoMIBObjects':ptopoMIBObjects,'ptopoConnData':ptopoConnData,'ptopoConnTable':ptopoConnTable,'ptopoConnEntry':ptopoConnEntry,_H:ptopoConnIndex,'ptopoConnLocalDevice':ptopoConnLocalDevice,'ptopoConnLocalPort':ptopoConnLocalPort,'ptopoConnRemoteDevice':ptopoConnRemoteDevice,'ptopoConnRemotePort':ptopoConnRemotePort,'ptopoConnIsUpStream':ptopoConnIsUpStream,'ptopoDevData':ptopoDevData,'ptopoDevTable':ptopoDevTable,'ptopoDevEntry':ptopoDevEntry,_I:ptopoDevID,'ptopoDevHostname':ptopoDevHostname,'ptopoDevClusStatus':ptopoDevClusStatus,'ptopoDevClusMode':ptopoDevClusMode,'ptopoDevClusName':ptopoDevClusName,'ptopoDevCSMac':ptopoDevCSMac,'ptopoDevHopsToCs':ptopoDevHopsToCs,'ptopoDevLastVerifyTime':ptopoDevLastVerifyTime,'ptopoConfig':ptopoConfig,'ptopoConfigInterval':ptopoConfigInterval,'ptopoConfigMaxHoldTime':ptopoConfigMaxHoldTime,'ptopoConfigHopCount':ptopoConfigHopCount})
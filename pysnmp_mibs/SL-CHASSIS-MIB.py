_H='slChassisSlotId'
_G='SL-CHASSIS-MIB'
_F='gneNode'
_E='DisplayString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
slMain,=mibBuilder.importSymbols('SL-MAIN-MIB','slMain')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
slChassis=ModuleIdentity((1,3,6,1,4,1,4515,1,3,18))
_SlChassisInfo_ObjectIdentity=ObjectIdentity
slChassisInfo=_SlChassisInfo_ObjectIdentity((1,3,6,1,4,1,4515,1,3,18,1))
_SlChassisInfoNodeSlotId_Type=Integer32
_SlChassisInfoNodeSlotId_Object=MibScalar
slChassisInfoNodeSlotId=_SlChassisInfoNodeSlotId_Object((1,3,6,1,4,1,4515,1,3,18,1,1),_SlChassisInfoNodeSlotId_Type())
slChassisInfoNodeSlotId.setMaxAccess(_C)
if mibBuilder.loadTexts:slChassisInfoNodeSlotId.setStatus(_A)
class _SlChassisInfoNodeRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('internalSlotNode',2),('none',3)))
_SlChassisInfoNodeRole_Type.__name__=_D
_SlChassisInfoNodeRole_Object=MibScalar
slChassisInfoNodeRole=_SlChassisInfoNodeRole_Object((1,3,6,1,4,1,4515,1,3,18,1,2),_SlChassisInfoNodeRole_Type())
slChassisInfoNodeRole.setMaxAccess(_C)
if mibBuilder.loadTexts:slChassisInfoNodeRole.setStatus(_A)
_SlChassisInfoLanVrrpIp_Type=IpAddress
_SlChassisInfoLanVrrpIp_Object=MibScalar
slChassisInfoLanVrrpIp=_SlChassisInfoLanVrrpIp_Object((1,3,6,1,4,1,4515,1,3,18,1,3),_SlChassisInfoLanVrrpIp_Type())
slChassisInfoLanVrrpIp.setMaxAccess(_C)
if mibBuilder.loadTexts:slChassisInfoLanVrrpIp.setStatus(_A)
_SlChassisInfoOscVrrpIp_Type=IpAddress
_SlChassisInfoOscVrrpIp_Object=MibScalar
slChassisInfoOscVrrpIp=_SlChassisInfoOscVrrpIp_Object((1,3,6,1,4,1,4515,1,3,18,1,4),_SlChassisInfoOscVrrpIp_Type())
slChassisInfoOscVrrpIp.setMaxAccess(_C)
if mibBuilder.loadTexts:slChassisInfoOscVrrpIp.setStatus(_A)
class _SlChassisInfoTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('osc',1),('lan',2),('simple',3)))
_SlChassisInfoTopology_Type.__name__=_D
_SlChassisInfoTopology_Object=MibScalar
slChassisInfoTopology=_SlChassisInfoTopology_Object((1,3,6,1,4,1,4515,1,3,18,1,5),_SlChassisInfoTopology_Type())
slChassisInfoTopology.setMaxAccess(_C)
if mibBuilder.loadTexts:slChassisInfoTopology.setStatus(_A)
class _SlChassisInfoVrrpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_SlChassisInfoVrrpEnable_Type.__name__=_D
_SlChassisInfoVrrpEnable_Object=MibScalar
slChassisInfoVrrpEnable=_SlChassisInfoVrrpEnable_Object((1,3,6,1,4,1,4515,1,3,18,1,6),_SlChassisInfoVrrpEnable_Type())
slChassisInfoVrrpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:slChassisInfoVrrpEnable.setStatus(_A)
_SlChassisSlot_ObjectIdentity=ObjectIdentity
slChassisSlot=_SlChassisSlot_ObjectIdentity((1,3,6,1,4,1,4515,1,3,18,2))
_SlChassisSlotTable_Object=MibTable
slChassisSlotTable=_SlChassisSlotTable_Object((1,3,6,1,4,1,4515,1,3,18,2,1))
if mibBuilder.loadTexts:slChassisSlotTable.setStatus(_A)
_SlChassisSlotEntry_Object=MibTableRow
slChassisSlotEntry=_SlChassisSlotEntry_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1))
slChassisSlotEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:slChassisSlotEntry.setStatus(_A)
_SlChassisSlotId_Type=Integer32
_SlChassisSlotId_Object=MibTableColumn
slChassisSlotId=_SlChassisSlotId_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,1),_SlChassisSlotId_Type())
slChassisSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotId.setStatus(_A)
class _SlChassisSlotRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('internalNode',2)))
_SlChassisSlotRole_Type.__name__=_D
_SlChassisSlotRole_Object=MibTableColumn
slChassisSlotRole=_SlChassisSlotRole_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,2),_SlChassisSlotRole_Type())
slChassisSlotRole.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotRole.setStatus(_A)
_SlChassisSlotInternalIp_Type=IpAddress
_SlChassisSlotInternalIp_Object=MibTableColumn
slChassisSlotInternalIp=_SlChassisSlotInternalIp_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,3),_SlChassisSlotInternalIp_Type())
slChassisSlotInternalIp.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotInternalIp.setStatus(_A)
_SlChassisSlotProductType_Type=ObjectIdentifier
_SlChassisSlotProductType_Object=MibTableColumn
slChassisSlotProductType=_SlChassisSlotProductType_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,4),_SlChassisSlotProductType_Type())
slChassisSlotProductType.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotProductType.setStatus(_A)
class _SlChassisSlotSysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SlChassisSlotSysName_Type.__name__=_E
_SlChassisSlotSysName_Object=MibTableColumn
slChassisSlotSysName=_SlChassisSlotSysName_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,5),_SlChassisSlotSysName_Type())
slChassisSlotSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotSysName.setStatus(_A)
_SlChassisSlotSnmp161Port_Type=Integer32
_SlChassisSlotSnmp161Port_Object=MibTableColumn
slChassisSlotSnmp161Port=_SlChassisSlotSnmp161Port_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,6),_SlChassisSlotSnmp161Port_Type())
slChassisSlotSnmp161Port.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotSnmp161Port.setStatus(_A)
_SlChassisSlotSnmp162MinPort_Type=Integer32
_SlChassisSlotSnmp162MinPort_Object=MibTableColumn
slChassisSlotSnmp162MinPort=_SlChassisSlotSnmp162MinPort_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,7),_SlChassisSlotSnmp162MinPort_Type())
slChassisSlotSnmp162MinPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotSnmp162MinPort.setStatus(_A)
_SlChassisSlotSnmp162MaxPort_Type=Integer32
_SlChassisSlotSnmp162MaxPort_Object=MibTableColumn
slChassisSlotSnmp162MaxPort=_SlChassisSlotSnmp162MaxPort_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,8),_SlChassisSlotSnmp162MaxPort_Type())
slChassisSlotSnmp162MaxPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotSnmp162MaxPort.setStatus(_A)
_SlChassisSlotHttpPort_Type=Integer32
_SlChassisSlotHttpPort_Object=MibTableColumn
slChassisSlotHttpPort=_SlChassisSlotHttpPort_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,9),_SlChassisSlotHttpPort_Type())
slChassisSlotHttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotHttpPort.setStatus(_A)
_SlChassisSlotTelnetPort_Type=Integer32
_SlChassisSlotTelnetPort_Object=MibTableColumn
slChassisSlotTelnetPort=_SlChassisSlotTelnetPort_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,10),_SlChassisSlotTelnetPort_Type())
slChassisSlotTelnetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotTelnetPort.setStatus(_A)
_SlChassisSlotFtpPort_Type=Integer32
_SlChassisSlotFtpPort_Object=MibTableColumn
slChassisSlotFtpPort=_SlChassisSlotFtpPort_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,12),_SlChassisSlotFtpPort_Type())
slChassisSlotFtpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotFtpPort.setStatus(_A)
_SlChassisSlotTL1Port_Type=Integer32
_SlChassisSlotTL1Port_Object=MibTableColumn
slChassisSlotTL1Port=_SlChassisSlotTL1Port_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,13),_SlChassisSlotTL1Port_Type())
slChassisSlotTL1Port.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotTL1Port.setStatus(_A)
_SlChassisSlotPingIdentifier_Type=Integer32
_SlChassisSlotPingIdentifier_Object=MibTableColumn
slChassisSlotPingIdentifier=_SlChassisSlotPingIdentifier_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,14),_SlChassisSlotPingIdentifier_Type())
slChassisSlotPingIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotPingIdentifier.setStatus(_A)
_SlChassisSlotHttpsPort_Type=Integer32
_SlChassisSlotHttpsPort_Object=MibTableColumn
slChassisSlotHttpsPort=_SlChassisSlotHttpsPort_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,15),_SlChassisSlotHttpsPort_Type())
slChassisSlotHttpsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotHttpsPort.setStatus(_A)
_SlChassisSlotSshPort_Type=Integer32
_SlChassisSlotSshPort_Object=MibTableColumn
slChassisSlotSshPort=_SlChassisSlotSshPort_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,16),_SlChassisSlotSshPort_Type())
slChassisSlotSshPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotSshPort.setStatus(_A)
_SlChassisSlotSTL1Port_Type=Integer32
_SlChassisSlotSTL1Port_Object=MibTableColumn
slChassisSlotSTL1Port=_SlChassisSlotSTL1Port_Object((1,3,6,1,4,1,4515,1,3,18,2,1,1,17),_SlChassisSlotSTL1Port_Type())
slChassisSlotSTL1Port.setMaxAccess(_B)
if mibBuilder.loadTexts:slChassisSlotSTL1Port.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'slChassis':slChassis,'slChassisInfo':slChassisInfo,'slChassisInfoNodeSlotId':slChassisInfoNodeSlotId,'slChassisInfoNodeRole':slChassisInfoNodeRole,'slChassisInfoLanVrrpIp':slChassisInfoLanVrrpIp,'slChassisInfoOscVrrpIp':slChassisInfoOscVrrpIp,'slChassisInfoTopology':slChassisInfoTopology,'slChassisInfoVrrpEnable':slChassisInfoVrrpEnable,'slChassisSlot':slChassisSlot,'slChassisSlotTable':slChassisSlotTable,'slChassisSlotEntry':slChassisSlotEntry,_H:slChassisSlotId,'slChassisSlotRole':slChassisSlotRole,'slChassisSlotInternalIp':slChassisSlotInternalIp,'slChassisSlotProductType':slChassisSlotProductType,'slChassisSlotSysName':slChassisSlotSysName,'slChassisSlotSnmp161Port':slChassisSlotSnmp161Port,'slChassisSlotSnmp162MinPort':slChassisSlotSnmp162MinPort,'slChassisSlotSnmp162MaxPort':slChassisSlotSnmp162MaxPort,'slChassisSlotHttpPort':slChassisSlotHttpPort,'slChassisSlotTelnetPort':slChassisSlotTelnetPort,'slChassisSlotFtpPort':slChassisSlotFtpPort,'slChassisSlotTL1Port':slChassisSlotTL1Port,'slChassisSlotPingIdentifier':slChassisSlotPingIdentifier,'slChassisSlotHttpsPort':slChassisSlotHttpsPort,'slChassisSlotSshPort':slChassisSlotSshPort,'slChassisSlotSTL1Port':slChassisSlotSTL1Port})
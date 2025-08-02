_G='read-write'
_F='a2Actionname'
_E='Integer32'
_D='DmiComponentIndex'
_C='DELLLOCALRESPONSEAGENTMIF-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class DmiInteger(Integer32):0
class DmiDisplaystring(DisplayString):0
class DmiDate(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(28,28));fixedLength=28
class DmiComponentIndex(Integer32):0
_Dell_ObjectIdentity=ObjectIdentity
dell=_Dell_ObjectIdentity((1,3,6,1,4,1,674))
_Server_ObjectIdentity=ObjectIdentity
server=_Server_ObjectIdentity((1,3,6,1,4,1,674,10890))
_Localresponseagent_ObjectIdentity=ObjectIdentity
localresponseagent=_Localresponseagent_ObjectIdentity((1,3,6,1,4,1,674,10890,3))
_DmtfGroups_ObjectIdentity=ObjectIdentity
dmtfGroups=_DmtfGroups_ObjectIdentity((1,3,6,1,4,1,674,10890,3,1))
_TComponentid_Object=MibTable
tComponentid=_TComponentid_Object((1,3,6,1,4,1,674,10890,3,1,1))
if mibBuilder.loadTexts:tComponentid.setStatus(_A)
_EComponentid_Object=MibTableRow
eComponentid=_EComponentid_Object((1,3,6,1,4,1,674,10890,3,1,1,1))
eComponentid.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:eComponentid.setStatus(_A)
_A1Manufacturer_Type=DmiDisplaystring
_A1Manufacturer_Object=MibTableColumn
a1Manufacturer=_A1Manufacturer_Object((1,3,6,1,4,1,674,10890,3,1,1,1,1),_A1Manufacturer_Type())
a1Manufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:a1Manufacturer.setStatus(_A)
_A1Product_Type=DmiDisplaystring
_A1Product_Object=MibTableColumn
a1Product=_A1Product_Object((1,3,6,1,4,1,674,10890,3,1,1,1,2),_A1Product_Type())
a1Product.setMaxAccess(_B)
if mibBuilder.loadTexts:a1Product.setStatus(_A)
_A1Version_Type=DmiDisplaystring
_A1Version_Object=MibTableColumn
a1Version=_A1Version_Object((1,3,6,1,4,1,674,10890,3,1,1,1,3),_A1Version_Type())
a1Version.setMaxAccess(_B)
if mibBuilder.loadTexts:a1Version.setStatus(_A)
_A1SerialNumber_Type=DmiDisplaystring
_A1SerialNumber_Object=MibTableColumn
a1SerialNumber=_A1SerialNumber_Object((1,3,6,1,4,1,674,10890,3,1,1,1,4),_A1SerialNumber_Type())
a1SerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:a1SerialNumber.setStatus(_A)
_A1Installation_Type=DmiDate
_A1Installation_Object=MibTableColumn
a1Installation=_A1Installation_Object((1,3,6,1,4,1,674,10890,3,1,1,1,5),_A1Installation_Type())
a1Installation.setMaxAccess(_B)
if mibBuilder.loadTexts:a1Installation.setStatus(_A)
class _A1Verify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('vAnErrorOccurredCheckStatusCode',0),('vThisComponentDoesNotExist',1),('vTheVerifyIsNotSupported',2),('vReserved',3),('vThisComponentExistsButTheFunctionalityI',4),('vThisComponentExistsButTheFunctionality1',5),('vThisComponentExistsAndIsNotFunctioningC',6),('vThisComponentExistsAndIsFunctioningCorr',7)))
_A1Verify_Type.__name__=_E
_A1Verify_Object=MibTableColumn
a1Verify=_A1Verify_Object((1,3,6,1,4,1,674,10890,3,1,1,1,6),_A1Verify_Type())
a1Verify.setMaxAccess(_B)
if mibBuilder.loadTexts:a1Verify.setStatus(_A)
_TActionResponseTable_Object=MibTable
tActionResponseTable=_TActionResponseTable_Object((1,3,6,1,4,1,674,10890,3,1,2))
if mibBuilder.loadTexts:tActionResponseTable.setStatus(_A)
_EActionResponseTable_Object=MibTableRow
eActionResponseTable=_EActionResponseTable_Object((1,3,6,1,4,1,674,10890,3,1,2,1))
eActionResponseTable.setIndexNames((0,_C,_D),(0,_C,_F))
if mibBuilder.loadTexts:eActionResponseTable.setStatus(_A)
class _A2Actionname_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3,7,13,14,160,168,172,200,202,204,206,208,210,212,214,220,225)));namedValues=NamedValues(*(('vUnknown',0),('vAdaptec-HostAdapterFailed',3),('vAdaptec-LogicalUnitFailed',7),('vApc-SystemOnLowUtilityPower',13),('vApc-SystemOnLowBatteryPower',14),('vTemperatureSensorDetectedAFailure',160),('vFanSensorDetectedAFailure',168),('vVoltageSensorDetectedAFailure',172),('vTemperatureSensorWarningDetected',200),('vVoltageSensorWarningDetected',202),('vFanSensorWarningDetected',204),('vCurrentSensorDetectedAFailure',206),('vCurrentSensorWarningDetected',208),('vPowerSupplyLostRedundancyDetected',210),('vPowerSupplyDegradedRedundancyDetected',212),('vPowerSupplyDetectedAFailure',214),('vChassisIntrusionDetected',220),('vLostConnectionToDiskPod',225)))
_A2Actionname_Type.__name__=_E
_A2Actionname_Object=MibTableColumn
a2Actionname=_A2Actionname_Object((1,3,6,1,4,1,674,10890,3,1,2,1,1),_A2Actionname_Type())
a2Actionname.setMaxAccess(_B)
if mibBuilder.loadTexts:a2Actionname.setStatus(_A)
_A2Actionresponse_Type=DmiDisplaystring
_A2Actionresponse_Object=MibTableColumn
a2Actionresponse=_A2Actionresponse_Object((1,3,6,1,4,1,674,10890,3,1,2,1,2),_A2Actionresponse_Type())
a2Actionresponse.setMaxAccess(_G)
if mibBuilder.loadTexts:a2Actionresponse.setStatus(_A)
_A2Actionexecute_Type=DmiDisplaystring
_A2Actionexecute_Object=MibTableColumn
a2Actionexecute=_A2Actionexecute_Object((1,3,6,1,4,1,674,10890,3,1,2,1,3),_A2Actionexecute_Type())
a2Actionexecute.setMaxAccess(_G)
if mibBuilder.loadTexts:a2Actionexecute.setStatus(_A)
_A2Actionsource_Type=DmiDisplaystring
_A2Actionsource_Object=MibTableColumn
a2Actionsource=_A2Actionsource_Object((1,3,6,1,4,1,674,10890,3,1,2,1,4),_A2Actionsource_Type())
a2Actionsource.setMaxAccess(_B)
if mibBuilder.loadTexts:a2Actionsource.setStatus(_A)
_TActionCapabilities_Object=MibTable
tActionCapabilities=_TActionCapabilities_Object((1,3,6,1,4,1,674,10890,3,1,3))
if mibBuilder.loadTexts:tActionCapabilities.setStatus(_A)
_EActionCapabilities_Object=MibTableRow
eActionCapabilities=_EActionCapabilities_Object((1,3,6,1,4,1,674,10890,3,1,3,1))
eActionCapabilities.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:eActionCapabilities.setStatus(_A)
_A3LraCapabilities_Type=DmiInteger
_A3LraCapabilities_Object=MibTableColumn
a3LraCapabilities=_A3LraCapabilities_Object((1,3,6,1,4,1,674,10890,3,1,3,1,1),_A3LraCapabilities_Type())
a3LraCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:a3LraCapabilities.setStatus(_A)
_TMiftomib_Object=MibTable
tMiftomib=_TMiftomib_Object((1,3,6,1,4,1,674,10890,3,1,99))
if mibBuilder.loadTexts:tMiftomib.setStatus(_A)
_EMiftomib_Object=MibTableRow
eMiftomib=_EMiftomib_Object((1,3,6,1,4,1,674,10890,3,1,99,1))
eMiftomib.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:eMiftomib.setStatus(_A)
_A99DellLocalResponseAgentMib_Type=DmiDisplaystring
_A99DellLocalResponseAgentMib_Object=MibTableColumn
a99DellLocalResponseAgentMib=_A99DellLocalResponseAgentMib_Object((1,3,6,1,4,1,674,10890,3,1,99,1,1),_A99DellLocalResponseAgentMib_Type())
a99DellLocalResponseAgentMib.setMaxAccess(_B)
if mibBuilder.loadTexts:a99DellLocalResponseAgentMib.setStatus(_A)
_A99MibOid_Type=DmiDisplaystring
_A99MibOid_Object=MibTableColumn
a99MibOid=_A99MibOid_Object((1,3,6,1,4,1,674,10890,3,1,99,1,2),_A99MibOid_Type())
a99MibOid.setMaxAccess(_B)
if mibBuilder.loadTexts:a99MibOid.setStatus(_A)
_A99DisableTraps_Type=DmiInteger
_A99DisableTraps_Object=MibTableColumn
a99DisableTraps=_A99DisableTraps_Object((1,3,6,1,4,1,674,10890,3,1,99,1,3),_A99DisableTraps_Type())
a99DisableTraps.setMaxAccess(_B)
if mibBuilder.loadTexts:a99DisableTraps.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'DmiInteger':DmiInteger,'DmiDisplaystring':DmiDisplaystring,'DmiDate':DmiDate,_D:DmiComponentIndex,'dell':dell,'server':server,'localresponseagent':localresponseagent,'dmtfGroups':dmtfGroups,'tComponentid':tComponentid,'eComponentid':eComponentid,'a1Manufacturer':a1Manufacturer,'a1Product':a1Product,'a1Version':a1Version,'a1SerialNumber':a1SerialNumber,'a1Installation':a1Installation,'a1Verify':a1Verify,'tActionResponseTable':tActionResponseTable,'eActionResponseTable':eActionResponseTable,_F:a2Actionname,'a2Actionresponse':a2Actionresponse,'a2Actionexecute':a2Actionexecute,'a2Actionsource':a2Actionsource,'tActionCapabilities':tActionCapabilities,'eActionCapabilities':eActionCapabilities,'a3LraCapabilities':a3LraCapabilities,'tMiftomib':tMiftomib,'eMiftomib':eMiftomib,'a99DellLocalResponseAgentMib':a99DellLocalResponseAgentMib,'a99MibOid':a99MibOid,'a99DisableTraps':a99DisableTraps})
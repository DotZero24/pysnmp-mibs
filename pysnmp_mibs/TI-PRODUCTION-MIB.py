_S='modemProdUsCmfIndex'
_R='modemProdUsPgaAttenIndex'
_Q='modemProdUsFreqCalibrationIndex'
_P='modemProdUsCalibrationIndex'
_O='modemProdUsTransmitlIndex'
_N='modemProdDsCallIndex'
_M='japanese'
_L='european'
_K='northAmerican'
_J='dBmV'
_I='herz'
_H='DisplayString'
_G='not-accessible'
_F='unknown'
_E='TI-PRODUCTION-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DocsisUpstreamType,=mibBuilder.importSymbols('DOCS-IF-MIB','DocsisUpstreamType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_H,'MacAddress','PhysAddress','TextualConvention','TruthValue')
eqName,=mibBuilder.importSymbols('TI-MANUFACTURER-MIB','eqName')
modemProduction=ModuleIdentity((1,3,6,1,4,1,294,1,400,2))
_ModemProdCmSetup_ObjectIdentity=ObjectIdentity
modemProdCmSetup=_ModemProdCmSetup_ObjectIdentity((1,3,6,1,4,1,294,1,400,2,1))
_ModemProdCmPermanentSetup_ObjectIdentity=ObjectIdentity
modemProdCmPermanentSetup=_ModemProdCmPermanentSetup_ObjectIdentity((1,3,6,1,4,1,294,1,400,2,1,1))
_ModemProdCmCertServerIp_Type=IpAddress
_ModemProdCmCertServerIp_Object=MibScalar
modemProdCmCertServerIp=_ModemProdCmCertServerIp_Object((1,3,6,1,4,1,294,1,400,2,1,1,1),_ModemProdCmCertServerIp_Type())
modemProdCmCertServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdCmCertServerIp.setStatus(_A)
class _ModemProdCmCertFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_ModemProdCmCertFileName_Type.__name__=_H
_ModemProdCmCertFileName_Object=MibScalar
modemProdCmCertFileName=_ModemProdCmCertFileName_Object((1,3,6,1,4,1,294,1,400,2,1,1,2),_ModemProdCmCertFileName_Type())
modemProdCmCertFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdCmCertFileName.setStatus(_A)
class _ModemProdCmCertKeyFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_ModemProdCmCertKeyFileName_Type.__name__=_H
_ModemProdCmCertKeyFileName_Object=MibScalar
modemProdCmCertKeyFileName=_ModemProdCmCertKeyFileName_Object((1,3,6,1,4,1,294,1,400,2,1,1,3),_ModemProdCmCertKeyFileName_Type())
modemProdCmCertKeyFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdCmCertKeyFileName.setStatus(_A)
class _ModemProdCmCertFrequencyPlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_K,1),(_L,2),(_M,3)))
_ModemProdCmCertFrequencyPlan_Type.__name__=_C
_ModemProdCmCertFrequencyPlan_Object=MibScalar
modemProdCmCertFrequencyPlan=_ModemProdCmCertFrequencyPlan_Object((1,3,6,1,4,1,294,1,400,2,1,1,4),_ModemProdCmCertFrequencyPlan_Type())
modemProdCmCertFrequencyPlan.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdCmCertFrequencyPlan.setStatus(_A)
_ModemProdCmCertDownload_Type=TruthValue
_ModemProdCmCertDownload_Object=MibScalar
modemProdCmCertDownload=_ModemProdCmCertDownload_Object((1,3,6,1,4,1,294,1,400,2,1,1,5),_ModemProdCmCertDownload_Type())
modemProdCmCertDownload.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdCmCertDownload.setStatus(_A)
class _ModemProdCmCertOperStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),('downloadInProgress',1),('downloadSuccess',2),('downloadFailed',3)))
_ModemProdCmCertOperStat_Type.__name__=_C
_ModemProdCmCertOperStat_Object=MibScalar
modemProdCmCertOperStat=_ModemProdCmCertOperStat_Object((1,3,6,1,4,1,294,1,400,2,1,1,6),_ModemProdCmCertOperStat_Type())
modemProdCmCertOperStat.setMaxAccess(_D)
if mibBuilder.loadTexts:modemProdCmCertOperStat.setStatus(_A)
_ModemProdCmManufacturingSetup_ObjectIdentity=ObjectIdentity
modemProdCmManufacturingSetup=_ModemProdCmManufacturingSetup_ObjectIdentity((1,3,6,1,4,1,294,1,400,2,1,2))
class _ModemProdMibAccessControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('maxaccess',1),('limitedaccess',2),('nonaccessible',3)))
_ModemProdMibAccessControl_Type.__name__=_C
_ModemProdMibAccessControl_Object=MibScalar
modemProdMibAccessControl=_ModemProdMibAccessControl_Object((1,3,6,1,4,1,294,1,400,2,1,2,1),_ModemProdMibAccessControl_Type())
modemProdMibAccessControl.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdMibAccessControl.setStatus(_A)
class _ModemProdSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_ModemProdSerialNumber_Type.__name__=_H
_ModemProdSerialNumber_Object=MibScalar
modemProdSerialNumber=_ModemProdSerialNumber_Object((1,3,6,1,4,1,294,1,400,2,1,2,2),_ModemProdSerialNumber_Type())
modemProdSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:modemProdSerialNumber.setStatus(_A)
_ModemProdMtaEnable_Type=TruthValue
_ModemProdMtaEnable_Object=MibScalar
modemProdMtaEnable=_ModemProdMtaEnable_Object((1,3,6,1,4,1,294,1,400,2,1,2,3),_ModemProdMtaEnable_Type())
modemProdMtaEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdMtaEnable.setStatus(_A)
_ModemProdMfgOrganizationName_Type=DisplayString
_ModemProdMfgOrganizationName_Object=MibScalar
modemProdMfgOrganizationName=_ModemProdMfgOrganizationName_Object((1,3,6,1,4,1,294,1,400,2,1,2,4),_ModemProdMfgOrganizationName_Type())
modemProdMfgOrganizationName.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdMfgOrganizationName.setStatus(_A)
_ModemProdCvcAccessStart_Type=DateAndTime
_ModemProdCvcAccessStart_Object=MibScalar
modemProdCvcAccessStart=_ModemProdCvcAccessStart_Object((1,3,6,1,4,1,294,1,400,2,1,2,5),_ModemProdCvcAccessStart_Type())
modemProdCvcAccessStart.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdCvcAccessStart.setStatus(_A)
_ModemProdCodeAccessStart_Type=DateAndTime
_ModemProdCodeAccessStart_Object=MibScalar
modemProdCodeAccessStart=_ModemProdCodeAccessStart_Object((1,3,6,1,4,1,294,1,400,2,1,2,6),_ModemProdCodeAccessStart_Type())
modemProdCodeAccessStart.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdCodeAccessStart.setStatus(_A)
_ModemProdLanIp_Type=IpAddress
_ModemProdLanIp_Object=MibScalar
modemProdLanIp=_ModemProdLanIp_Object((1,3,6,1,4,1,294,1,400,2,1,2,7),_ModemProdLanIp_Type())
modemProdLanIp.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdLanIp.setStatus(_A)
_ModemProdHostIp_Type=IpAddress
_ModemProdHostIp_Object=MibScalar
modemProdHostIp=_ModemProdHostIp_Object((1,3,6,1,4,1,294,1,400,2,1,2,8),_ModemProdHostIp_Type())
modemProdHostIp.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdHostIp.setStatus(_A)
_ModemProdIpMask_Type=IpAddress
_ModemProdIpMask_Object=MibScalar
modemProdIpMask=_ModemProdIpMask_Object((1,3,6,1,4,1,294,1,400,2,1,2,9),_ModemProdIpMask_Type())
modemProdIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdIpMask.setStatus(_A)
_ModemProdInterfaceName_Type=DisplayString
_ModemProdInterfaceName_Object=MibScalar
modemProdInterfaceName=_ModemProdInterfaceName_Object((1,3,6,1,4,1,294,1,400,2,1,2,10),_ModemProdInterfaceName_Type())
modemProdInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdInterfaceName.setStatus(_A)
_ModemProdCmMacAddress_Type=MacAddress
_ModemProdCmMacAddress_Object=MibScalar
modemProdCmMacAddress=_ModemProdCmMacAddress_Object((1,3,6,1,4,1,294,1,400,2,1,2,11),_ModemProdCmMacAddress_Type())
modemProdCmMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdCmMacAddress.setStatus(_A)
_ModemProdLanMacAddress_Type=MacAddress
_ModemProdLanMacAddress_Object=MibScalar
modemProdLanMacAddress=_ModemProdLanMacAddress_Object((1,3,6,1,4,1,294,1,400,2,1,2,12),_ModemProdLanMacAddress_Type())
modemProdLanMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdLanMacAddress.setStatus(_A)
_ModemProdUsbDevMacAddress_Type=MacAddress
_ModemProdUsbDevMacAddress_Object=MibScalar
modemProdUsbDevMacAddress=_ModemProdUsbDevMacAddress_Object((1,3,6,1,4,1,294,1,400,2,1,2,13),_ModemProdUsbDevMacAddress_Type())
modemProdUsbDevMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdUsbDevMacAddress.setStatus(_A)
_ModemProdUsbHostMacAddress_Type=MacAddress
_ModemProdUsbHostMacAddress_Object=MibScalar
modemProdUsbHostMacAddress=_ModemProdUsbHostMacAddress_Object((1,3,6,1,4,1,294,1,400,2,1,2,14),_ModemProdUsbHostMacAddress_Type())
modemProdUsbHostMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdUsbHostMacAddress.setStatus(_A)
class _ModemProdBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_F,0),('br2400',1),('br4800',2),('br9600',3),('br19200',4),('br38400',5),('br115200',6)))
_ModemProdBaudRate_Type.__name__=_C
_ModemProdBaudRate_Object=MibScalar
modemProdBaudRate=_ModemProdBaudRate_Object((1,3,6,1,4,1,294,1,400,2,1,2,15),_ModemProdBaudRate_Type())
modemProdBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdBaudRate.setStatus(_A)
class _ModemProdTunersNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_ModemProdTunersNumber_Type.__name__=_C
_ModemProdTunersNumber_Object=MibScalar
modemProdTunersNumber=_ModemProdTunersNumber_Object((1,3,6,1,4,1,294,1,400,2,1,2,16),_ModemProdTunersNumber_Type())
modemProdTunersNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdTunersNumber.setStatus(_A)
_ModemProdDocsisPhyMultFact_Type=Integer32
_ModemProdDocsisPhyMultFact_Object=MibScalar
modemProdDocsisPhyMultFact=_ModemProdDocsisPhyMultFact_Object((1,3,6,1,4,1,294,1,400,2,1,2,17),_ModemProdDocsisPhyMultFact_Type())
modemProdDocsisPhyMultFact.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdDocsisPhyMultFact.setStatus(_A)
class _ModemProdTunerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),('mt2060',1),('mt2064',2),('mt2068',3),('mt2170',4),('anadAt1061',5)))
_ModemProdTunerType_Type.__name__=_C
_ModemProdTunerType_Object=MibScalar
modemProdTunerType=_ModemProdTunerType_Object((1,3,6,1,4,1,294,1,400,2,1,2,18),_ModemProdTunerType_Type())
modemProdTunerType.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdTunerType.setStatus(_A)
class _ModemProdPgaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),('anadAra2017',1)))
_ModemProdPgaType_Type.__name__=_C
_ModemProdPgaType_Object=MibScalar
modemProdPgaType=_ModemProdPgaType_Object((1,3,6,1,4,1,294,1,400,2,1,2,19),_ModemProdPgaType_Type())
modemProdPgaType.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdPgaType.setStatus(_A)
_ModemProdHwRevision_Type=Integer32
_ModemProdHwRevision_Object=MibScalar
modemProdHwRevision=_ModemProdHwRevision_Object((1,3,6,1,4,1,294,1,400,2,1,2,20),_ModemProdHwRevision_Type())
modemProdHwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdHwRevision.setStatus(_A)
class _ModemProdFrequencyPlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),(_K,1),(_L,2),(_M,3),('hybrid',4)))
_ModemProdFrequencyPlan_Type.__name__=_C
_ModemProdFrequencyPlan_Object=MibScalar
modemProdFrequencyPlan=_ModemProdFrequencyPlan_Object((1,3,6,1,4,1,294,1,400,2,1,2,21),_ModemProdFrequencyPlan_Type())
modemProdFrequencyPlan.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdFrequencyPlan.setStatus(_A)
_ModemProdEnableCli_Type=TruthValue
_ModemProdEnableCli_Object=MibScalar
modemProdEnableCli=_ModemProdEnableCli_Object((1,3,6,1,4,1,294,1,400,2,1,2,22),_ModemProdEnableCli_Type())
modemProdEnableCli.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdEnableCli.setStatus(_A)
_ModemProdCmCalibrationSetup_ObjectIdentity=ObjectIdentity
modemProdCmCalibrationSetup=_ModemProdCmCalibrationSetup_ObjectIdentity((1,3,6,1,4,1,294,1,400,2,1,3))
_ModemProdDownstreamCalibration_ObjectIdentity=ObjectIdentity
modemProdDownstreamCalibration=_ModemProdDownstreamCalibration_ObjectIdentity((1,3,6,1,4,1,294,1,400,2,1,3,1))
class _ModemProdDsCalibrationOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('emptyTable',1),('completeTable',2),('callibrationInProgress',3),('callibrationComplete',4)))
_ModemProdDsCalibrationOperStatus_Type.__name__=_C
_ModemProdDsCalibrationOperStatus_Object=MibScalar
modemProdDsCalibrationOperStatus=_ModemProdDsCalibrationOperStatus_Object((1,3,6,1,4,1,294,1,400,2,1,3,1,1),_ModemProdDsCalibrationOperStatus_Type())
modemProdDsCalibrationOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:modemProdDsCalibrationOperStatus.setStatus(_A)
class _ModemProdDsCalibrationAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('validateAndStart',1),('validateOnly',2),('startOnly',3),('erase',4)))
_ModemProdDsCalibrationAdminStatus_Type.__name__=_C
_ModemProdDsCalibrationAdminStatus_Object=MibScalar
modemProdDsCalibrationAdminStatus=_ModemProdDsCalibrationAdminStatus_Object((1,3,6,1,4,1,294,1,400,2,1,3,1,2),_ModemProdDsCalibrationAdminStatus_Type())
modemProdDsCalibrationAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdDsCalibrationAdminStatus.setStatus(_A)
_ModemProdPowerCalibrationTable_Object=MibTable
modemProdPowerCalibrationTable=_ModemProdPowerCalibrationTable_Object((1,3,6,1,4,1,294,1,400,2,1,3,1,3))
if mibBuilder.loadTexts:modemProdPowerCalibrationTable.setStatus(_A)
_ModemProdPowerCalibrationEntry_Object=MibTableRow
modemProdPowerCalibrationEntry=_ModemProdPowerCalibrationEntry_Object((1,3,6,1,4,1,294,1,400,2,1,3,1,3,1))
modemProdPowerCalibrationEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:modemProdPowerCalibrationEntry.setStatus(_A)
class _ModemProdDsCallIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ModemProdDsCallIndex_Type.__name__=_C
_ModemProdDsCallIndex_Object=MibTableColumn
modemProdDsCallIndex=_ModemProdDsCallIndex_Object((1,3,6,1,4,1,294,1,400,2,1,3,1,3,1,1),_ModemProdDsCallIndex_Type())
modemProdDsCallIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:modemProdDsCallIndex.setStatus(_A)
class _ModemProdDsFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(80000,1300000))
_ModemProdDsFrequency_Type.__name__=_C
_ModemProdDsFrequency_Object=MibTableColumn
modemProdDsFrequency=_ModemProdDsFrequency_Object((1,3,6,1,4,1,294,1,400,2,1,3,1,3,1,2),_ModemProdDsFrequency_Type())
modemProdDsFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdDsFrequency.setStatus(_A)
if mibBuilder.loadTexts:modemProdDsFrequency.setUnits(_I)
class _ModemProdDsPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-700,700))
_ModemProdDsPower_Type.__name__=_C
_ModemProdDsPower_Object=MibTableColumn
modemProdDsPower=_ModemProdDsPower_Object((1,3,6,1,4,1,294,1,400,2,1,3,1,3,1,3),_ModemProdDsPower_Type())
modemProdDsPower.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdDsPower.setStatus(_A)
if mibBuilder.loadTexts:modemProdDsPower.setUnits('0.01 dbmV')
_ModemProdUpstreamTransmit_ObjectIdentity=ObjectIdentity
modemProdUpstreamTransmit=_ModemProdUpstreamTransmit_ObjectIdentity((1,3,6,1,4,1,294,1,400,2,1,3,2))
_ModemProdUpTransGain_Type=Integer32
_ModemProdUpTransGain_Object=MibScalar
modemProdUpTransGain=_ModemProdUpTransGain_Object((1,3,6,1,4,1,294,1,400,2,1,3,2,1),_ModemProdUpTransGain_Type())
modemProdUpTransGain.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdUpTransGain.setStatus(_A)
_ModemProdUpstreamTransmitTable_Object=MibTable
modemProdUpstreamTransmitTable=_ModemProdUpstreamTransmitTable_Object((1,3,6,1,4,1,294,1,400,2,1,3,2,2))
if mibBuilder.loadTexts:modemProdUpstreamTransmitTable.setStatus(_A)
_ModemProdUpstreamTransmitEntry_Object=MibTableRow
modemProdUpstreamTransmitEntry=_ModemProdUpstreamTransmitEntry_Object((1,3,6,1,4,1,294,1,400,2,1,3,2,2,1))
modemProdUpstreamTransmitEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:modemProdUpstreamTransmitEntry.setStatus(_A)
class _ModemProdUsTransmitlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ModemProdUsTransmitlIndex_Type.__name__=_C
_ModemProdUsTransmitlIndex_Object=MibTableColumn
modemProdUsTransmitlIndex=_ModemProdUsTransmitlIndex_Object((1,3,6,1,4,1,294,1,400,2,1,3,2,2,1,1),_ModemProdUsTransmitlIndex_Type())
modemProdUsTransmitlIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:modemProdUsTransmitlIndex.setStatus(_A)
_ModemProdUsFrequency_Type=Integer32
_ModemProdUsFrequency_Object=MibTableColumn
modemProdUsFrequency=_ModemProdUsFrequency_Object((1,3,6,1,4,1,294,1,400,2,1,3,2,2,1,2),_ModemProdUsFrequency_Type())
modemProdUsFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdUsFrequency.setStatus(_A)
if mibBuilder.loadTexts:modemProdUsFrequency.setUnits(_I)
class _ModemProdUsModulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('qpsk',1),('qam8',2),('qam16',3),('qam32',4),('qam64',5),('qam128',6),('qam256',7)))
_ModemProdUsModulation_Type.__name__=_C
_ModemProdUsModulation_Object=MibTableColumn
modemProdUsModulation=_ModemProdUsModulation_Object((1,3,6,1,4,1,294,1,400,2,1,3,2,2,1,3),_ModemProdUsModulation_Type())
modemProdUsModulation.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdUsModulation.setStatus(_A)
class _ModemProdUsSymbolRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('sr1',1),('sr2',2),('sr4',3),('sr8',4),('sr16',5),('sr32',6)))
_ModemProdUsSymbolRate_Type.__name__=_C
_ModemProdUsSymbolRate_Object=MibTableColumn
modemProdUsSymbolRate=_ModemProdUsSymbolRate_Object((1,3,6,1,4,1,294,1,400,2,1,3,2,2,1,4),_ModemProdUsSymbolRate_Type())
modemProdUsSymbolRate.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdUsSymbolRate.setStatus(_A)
_ModemProdUsAttenuation_Type=Integer32
_ModemProdUsAttenuation_Object=MibTableColumn
modemProdUsAttenuation=_ModemProdUsAttenuation_Object((1,3,6,1,4,1,294,1,400,2,1,3,2,2,1,5),_ModemProdUsAttenuation_Type())
modemProdUsAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdUsAttenuation.setStatus(_A)
if mibBuilder.loadTexts:modemProdUsAttenuation.setUnits('dB')
class _ModemProdUsTransmitionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stop',1),('data',2),('syn',3)))
_ModemProdUsTransmitionType_Type.__name__=_C
_ModemProdUsTransmitionType_Object=MibTableColumn
modemProdUsTransmitionType=_ModemProdUsTransmitionType_Object((1,3,6,1,4,1,294,1,400,2,1,3,2,2,1,6),_ModemProdUsTransmitionType_Type())
modemProdUsTransmitionType.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdUsTransmitionType.setStatus(_A)
_ModemProdUsBurst_Type=Integer32
_ModemProdUsBurst_Object=MibTableColumn
modemProdUsBurst=_ModemProdUsBurst_Object((1,3,6,1,4,1,294,1,400,2,1,3,2,2,1,7),_ModemProdUsBurst_Type())
modemProdUsBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdUsBurst.setStatus(_A)
_ModemProdUpstreamCalibration_ObjectIdentity=ObjectIdentity
modemProdUpstreamCalibration=_ModemProdUpstreamCalibration_ObjectIdentity((1,3,6,1,4,1,294,1,400,2,1,3,3))
class _ModemProdUsCalibrationTableErase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pgaParams',1),('cmfParams',2),('freqParams',3),('allTables',4)))
_ModemProdUsCalibrationTableErase_Type.__name__=_C
_ModemProdUsCalibrationTableErase_Object=MibScalar
modemProdUsCalibrationTableErase=_ModemProdUsCalibrationTableErase_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,1),_ModemProdUsCalibrationTableErase_Type())
modemProdUsCalibrationTableErase.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdUsCalibrationTableErase.setStatus(_A)
class _ModemProdUsCalibrationModeFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_ModemProdUsCalibrationModeFactor_Type.__name__=_C
_ModemProdUsCalibrationModeFactor_Object=MibScalar
modemProdUsCalibrationModeFactor=_ModemProdUsCalibrationModeFactor_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,2),_ModemProdUsCalibrationModeFactor_Type())
modemProdUsCalibrationModeFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdUsCalibrationModeFactor.setStatus(_A)
_ModemProdUsCalibrationPowerDelta_Type=Integer32
_ModemProdUsCalibrationPowerDelta_Object=MibScalar
modemProdUsCalibrationPowerDelta=_ModemProdUsCalibrationPowerDelta_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,3),_ModemProdUsCalibrationPowerDelta_Type())
modemProdUsCalibrationPowerDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdUsCalibrationPowerDelta.setStatus(_A)
if mibBuilder.loadTexts:modemProdUsCalibrationPowerDelta.setUnits('dB')
_ModemProdUpstreamCalibrationTable_Object=MibTable
modemProdUpstreamCalibrationTable=_ModemProdUpstreamCalibrationTable_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,4))
if mibBuilder.loadTexts:modemProdUpstreamCalibrationTable.setStatus(_A)
_ModemProdUpstreamCalibrationEntry_Object=MibTableRow
modemProdUpstreamCalibrationEntry=_ModemProdUpstreamCalibrationEntry_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,4,1))
modemProdUpstreamCalibrationEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:modemProdUpstreamCalibrationEntry.setStatus(_A)
class _ModemProdUsCalibrationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ModemProdUsCalibrationIndex_Type.__name__=_C
_ModemProdUsCalibrationIndex_Object=MibTableColumn
modemProdUsCalibrationIndex=_ModemProdUsCalibrationIndex_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,4,1,1),_ModemProdUsCalibrationIndex_Type())
modemProdUsCalibrationIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:modemProdUsCalibrationIndex.setStatus(_A)
_ModemProdUsCalibrationPower_Type=Integer32
_ModemProdUsCalibrationPower_Object=MibTableColumn
modemProdUsCalibrationPower=_ModemProdUsCalibrationPower_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,4,1,2),_ModemProdUsCalibrationPower_Type())
modemProdUsCalibrationPower.setMaxAccess(_D)
if mibBuilder.loadTexts:modemProdUsCalibrationPower.setStatus(_A)
if mibBuilder.loadTexts:modemProdUsCalibrationPower.setUnits('dB')
_ModemProdFrequencyCalibrationTable_Object=MibTable
modemProdFrequencyCalibrationTable=_ModemProdFrequencyCalibrationTable_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,5))
if mibBuilder.loadTexts:modemProdFrequencyCalibrationTable.setStatus(_A)
_ModemProdFrequencyCalibrationEntry_Object=MibTableRow
modemProdFrequencyCalibrationEntry=_ModemProdFrequencyCalibrationEntry_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,5,1))
modemProdFrequencyCalibrationEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:modemProdFrequencyCalibrationEntry.setStatus(_A)
_ModemProdUsFreqCalibrationIndex_Type=Integer32
_ModemProdUsFreqCalibrationIndex_Object=MibTableColumn
modemProdUsFreqCalibrationIndex=_ModemProdUsFreqCalibrationIndex_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,5,1,1),_ModemProdUsFreqCalibrationIndex_Type())
modemProdUsFreqCalibrationIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:modemProdUsFreqCalibrationIndex.setStatus(_A)
if mibBuilder.loadTexts:modemProdUsFreqCalibrationIndex.setUnits(_I)
_ModemProdUsFreqCalibrationPower_Type=Integer32
_ModemProdUsFreqCalibrationPower_Object=MibTableColumn
modemProdUsFreqCalibrationPower=_ModemProdUsFreqCalibrationPower_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,5,1,2),_ModemProdUsFreqCalibrationPower_Type())
modemProdUsFreqCalibrationPower.setMaxAccess(_D)
if mibBuilder.loadTexts:modemProdUsFreqCalibrationPower.setStatus(_A)
if mibBuilder.loadTexts:modemProdUsFreqCalibrationPower.setUnits(_J)
_ModemProdPgaAttenuationTable_Object=MibTable
modemProdPgaAttenuationTable=_ModemProdPgaAttenuationTable_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,6))
if mibBuilder.loadTexts:modemProdPgaAttenuationTable.setStatus(_A)
_ModemProdPgaAttenuationEntry_Object=MibTableRow
modemProdPgaAttenuationEntry=_ModemProdPgaAttenuationEntry_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,6,1))
modemProdPgaAttenuationEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:modemProdPgaAttenuationEntry.setStatus(_A)
class _ModemProdUsPgaAttenIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('pgaAtten0dB',1),('pgaAtten2dB',2),('pgaAtten4dB',3),('pgaAtten8dB',4),('pgaAtten16dB',5),('pgaAtten32dBb',6)))
_ModemProdUsPgaAttenIndex_Type.__name__=_C
_ModemProdUsPgaAttenIndex_Object=MibTableColumn
modemProdUsPgaAttenIndex=_ModemProdUsPgaAttenIndex_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,6,1,1),_ModemProdUsPgaAttenIndex_Type())
modemProdUsPgaAttenIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:modemProdUsPgaAttenIndex.setStatus(_A)
_ModemProdUsPgaAttenPower_Type=Integer32
_ModemProdUsPgaAttenPower_Object=MibTableColumn
modemProdUsPgaAttenPower=_ModemProdUsPgaAttenPower_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,6,1,2),_ModemProdUsPgaAttenPower_Type())
modemProdUsPgaAttenPower.setMaxAccess(_D)
if mibBuilder.loadTexts:modemProdUsPgaAttenPower.setStatus(_A)
if mibBuilder.loadTexts:modemProdUsPgaAttenPower.setUnits(_J)
_ModemProdCurrentModeFactorTable_Object=MibTable
modemProdCurrentModeFactorTable=_ModemProdCurrentModeFactorTable_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,7))
if mibBuilder.loadTexts:modemProdCurrentModeFactorTable.setStatus(_A)
_ModemProdCurrentModeFactorEntry_Object=MibTableRow
modemProdCurrentModeFactorEntry=_ModemProdCurrentModeFactorEntry_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,7,1))
modemProdCurrentModeFactorEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:modemProdCurrentModeFactorEntry.setStatus(_A)
class _ModemProdUsCmfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_ModemProdUsCmfIndex_Type.__name__=_C
_ModemProdUsCmfIndex_Object=MibTableColumn
modemProdUsCmfIndex=_ModemProdUsCmfIndex_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,7,1,1),_ModemProdUsCmfIndex_Type())
modemProdUsCmfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:modemProdUsCmfIndex.setStatus(_A)
_ModemProdUsCmfPower_Type=Integer32
_ModemProdUsCmfPower_Object=MibTableColumn
modemProdUsCmfPower=_ModemProdUsCmfPower_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,7,1,2),_ModemProdUsCmfPower_Type())
modemProdUsCmfPower.setMaxAccess(_D)
if mibBuilder.loadTexts:modemProdUsCmfPower.setStatus(_A)
if mibBuilder.loadTexts:modemProdUsCmfPower.setUnits(_J)
_ModemProdUsCalibrationUpdateFlash_Type=TruthValue
_ModemProdUsCalibrationUpdateFlash_Object=MibScalar
modemProdUsCalibrationUpdateFlash=_ModemProdUsCalibrationUpdateFlash_Object((1,3,6,1,4,1,294,1,400,2,1,3,3,8),_ModemProdUsCalibrationUpdateFlash_Type())
modemProdUsCalibrationUpdateFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:modemProdUsCalibrationUpdateFlash.setStatus(_A)
_ModemProdCmTest_ObjectIdentity=ObjectIdentity
modemProdCmTest=_ModemProdCmTest_ObjectIdentity((1,3,6,1,4,1,294,1,400,2,2))
mibBuilder.exportSymbols(_E,**{'modemProduction':modemProduction,'modemProdCmSetup':modemProdCmSetup,'modemProdCmPermanentSetup':modemProdCmPermanentSetup,'modemProdCmCertServerIp':modemProdCmCertServerIp,'modemProdCmCertFileName':modemProdCmCertFileName,'modemProdCmCertKeyFileName':modemProdCmCertKeyFileName,'modemProdCmCertFrequencyPlan':modemProdCmCertFrequencyPlan,'modemProdCmCertDownload':modemProdCmCertDownload,'modemProdCmCertOperStat':modemProdCmCertOperStat,'modemProdCmManufacturingSetup':modemProdCmManufacturingSetup,'modemProdMibAccessControl':modemProdMibAccessControl,'modemProdSerialNumber':modemProdSerialNumber,'modemProdMtaEnable':modemProdMtaEnable,'modemProdMfgOrganizationName':modemProdMfgOrganizationName,'modemProdCvcAccessStart':modemProdCvcAccessStart,'modemProdCodeAccessStart':modemProdCodeAccessStart,'modemProdLanIp':modemProdLanIp,'modemProdHostIp':modemProdHostIp,'modemProdIpMask':modemProdIpMask,'modemProdInterfaceName':modemProdInterfaceName,'modemProdCmMacAddress':modemProdCmMacAddress,'modemProdLanMacAddress':modemProdLanMacAddress,'modemProdUsbDevMacAddress':modemProdUsbDevMacAddress,'modemProdUsbHostMacAddress':modemProdUsbHostMacAddress,'modemProdBaudRate':modemProdBaudRate,'modemProdTunersNumber':modemProdTunersNumber,'modemProdDocsisPhyMultFact':modemProdDocsisPhyMultFact,'modemProdTunerType':modemProdTunerType,'modemProdPgaType':modemProdPgaType,'modemProdHwRevision':modemProdHwRevision,'modemProdFrequencyPlan':modemProdFrequencyPlan,'modemProdEnableCli':modemProdEnableCli,'modemProdCmCalibrationSetup':modemProdCmCalibrationSetup,'modemProdDownstreamCalibration':modemProdDownstreamCalibration,'modemProdDsCalibrationOperStatus':modemProdDsCalibrationOperStatus,'modemProdDsCalibrationAdminStatus':modemProdDsCalibrationAdminStatus,'modemProdPowerCalibrationTable':modemProdPowerCalibrationTable,'modemProdPowerCalibrationEntry':modemProdPowerCalibrationEntry,_N:modemProdDsCallIndex,'modemProdDsFrequency':modemProdDsFrequency,'modemProdDsPower':modemProdDsPower,'modemProdUpstreamTransmit':modemProdUpstreamTransmit,'modemProdUpTransGain':modemProdUpTransGain,'modemProdUpstreamTransmitTable':modemProdUpstreamTransmitTable,'modemProdUpstreamTransmitEntry':modemProdUpstreamTransmitEntry,_O:modemProdUsTransmitlIndex,'modemProdUsFrequency':modemProdUsFrequency,'modemProdUsModulation':modemProdUsModulation,'modemProdUsSymbolRate':modemProdUsSymbolRate,'modemProdUsAttenuation':modemProdUsAttenuation,'modemProdUsTransmitionType':modemProdUsTransmitionType,'modemProdUsBurst':modemProdUsBurst,'modemProdUpstreamCalibration':modemProdUpstreamCalibration,'modemProdUsCalibrationTableErase':modemProdUsCalibrationTableErase,'modemProdUsCalibrationModeFactor':modemProdUsCalibrationModeFactor,'modemProdUsCalibrationPowerDelta':modemProdUsCalibrationPowerDelta,'modemProdUpstreamCalibrationTable':modemProdUpstreamCalibrationTable,'modemProdUpstreamCalibrationEntry':modemProdUpstreamCalibrationEntry,_P:modemProdUsCalibrationIndex,'modemProdUsCalibrationPower':modemProdUsCalibrationPower,'modemProdFrequencyCalibrationTable':modemProdFrequencyCalibrationTable,'modemProdFrequencyCalibrationEntry':modemProdFrequencyCalibrationEntry,_Q:modemProdUsFreqCalibrationIndex,'modemProdUsFreqCalibrationPower':modemProdUsFreqCalibrationPower,'modemProdPgaAttenuationTable':modemProdPgaAttenuationTable,'modemProdPgaAttenuationEntry':modemProdPgaAttenuationEntry,_R:modemProdUsPgaAttenIndex,'modemProdUsPgaAttenPower':modemProdUsPgaAttenPower,'modemProdCurrentModeFactorTable':modemProdCurrentModeFactorTable,'modemProdCurrentModeFactorEntry':modemProdCurrentModeFactorEntry,_S:modemProdUsCmfIndex,'modemProdUsCmfPower':modemProdUsCmfPower,'modemProdUsCalibrationUpdateFlash':modemProdUsCalibrationUpdateFlash,'modemProdCmTest':modemProdCmTest})
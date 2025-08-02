_I='sfpDiagInterface'
_H='DisplayString'
_G='sfpConfigInterface'
_F='SL-SFP-MIB'
_E='SnmpAdminString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Float128TC,Float32TC,Float64TC=mibBuilder.importSymbols('FLOAT-TC-MIB','Float128TC','Float32TC','Float64TC')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
CleiCode,=mibBuilder.importSymbols('SL-ENTITY-MIB','CleiCode')
sitelight,=mibBuilder.importSymbols('SL-NE-MIB','sitelight')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention','TimeStamp','TruthValue')
slSfp=ModuleIdentity((1,3,6,1,4,1,4515,1,10))
_SfpConf_ObjectIdentity=ObjectIdentity
sfpConf=_SfpConf_ObjectIdentity((1,3,6,1,4,1,4515,1,10,1))
_SfpConfigTable_Object=MibTable
sfpConfigTable=_SfpConfigTable_Object((1,3,6,1,4,1,4515,1,10,1,1))
if mibBuilder.loadTexts:sfpConfigTable.setStatus(_A)
_SfpConfigEntry_Object=MibTableRow
sfpConfigEntry=_SfpConfigEntry_Object((1,3,6,1,4,1,4515,1,10,1,1,1))
sfpConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:sfpConfigEntry.setStatus(_A)
_SfpConfigInterface_Type=InterfaceIndex
_SfpConfigInterface_Object=MibTableColumn
sfpConfigInterface=_SfpConfigInterface_Object((1,3,6,1,4,1,4515,1,10,1,1,1,1),_SfpConfigInterface_Type())
sfpConfigInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigInterface.setStatus(_A)
class _SfpConfigXcvrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,6,11,12,13,14,15,16,17,20)));namedValues=NamedValues(*(('unknone',0),('gbic',1),('module',2),('sfp1310',3),('xfp',6),('sfpDwdm',11),('qsfp',12),('qsfpPlus',13),('cfp',14),('cxp',15),('coherent',16),('qsfp28',17),('cfp2',20)))
_SfpConfigXcvrId_Type.__name__=_D
_SfpConfigXcvrId_Object=MibTableColumn
sfpConfigXcvrId=_SfpConfigXcvrId_Object((1,3,6,1,4,1,4515,1,10,1,1,1,2),_SfpConfigXcvrId_Type())
sfpConfigXcvrId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXcvrId.setStatus(_A)
class _SfpConfig1310ExtXcvrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('modDef0',0),('modDef1',1),('modDef2',2),('modDef3',3),('modDef4',4),('modDef5',5),('modDef6',6),('modDef7',7)))
_SfpConfig1310ExtXcvrId_Type.__name__=_D
_SfpConfig1310ExtXcvrId_Object=MibTableColumn
sfpConfig1310ExtXcvrId=_SfpConfig1310ExtXcvrId_Object((1,3,6,1,4,1,4515,1,10,1,1,1,3),_SfpConfig1310ExtXcvrId_Type())
sfpConfig1310ExtXcvrId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfig1310ExtXcvrId.setStatus(_A)
_SfpConfigWdmExtXcvrId_Type=Integer32
_SfpConfigWdmExtXcvrId_Object=MibTableColumn
sfpConfigWdmExtXcvrId=_SfpConfigWdmExtXcvrId_Object((1,3,6,1,4,1,4515,1,10,1,1,1,4),_SfpConfigWdmExtXcvrId_Type())
sfpConfigWdmExtXcvrId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigWdmExtXcvrId.setStatus(_A)
class _SfpConfigConnectorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,32,33)));namedValues=NamedValues(*(('conUnknown',0),('conSc',1),('conFcCopper1',2),('conFcCopper2',3),('conBncTnc',4),('conFcCoaxial',5),('conFiberJack',6),('conLc',7),('conMtRj',8),('conMu',9),('comSg',10),('conOpticalPigtail',11),('conHssdc2',32),('conCopperPigtail',33)))
_SfpConfigConnectorCode_Type.__name__=_D
_SfpConfigConnectorCode_Object=MibTableColumn
sfpConfigConnectorCode=_SfpConfigConnectorCode_Object((1,3,6,1,4,1,4515,1,10,1,1,1,5),_SfpConfigConnectorCode_Type())
sfpConfigConnectorCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigConnectorCode.setStatus(_A)
_SfpConfigInfibandCompliance_Type=Integer32
_SfpConfigInfibandCompliance_Object=MibTableColumn
sfpConfigInfibandCompliance=_SfpConfigInfibandCompliance_Object((1,3,6,1,4,1,4515,1,10,1,1,1,6),_SfpConfigInfibandCompliance_Type())
sfpConfigInfibandCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigInfibandCompliance.setStatus(_A)
_SfpConfigEsconCompliance_Type=Integer32
_SfpConfigEsconCompliance_Object=MibTableColumn
sfpConfigEsconCompliance=_SfpConfigEsconCompliance_Object((1,3,6,1,4,1,4515,1,10,1,1,1,7),_SfpConfigEsconCompliance_Type())
sfpConfigEsconCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigEsconCompliance.setStatus(_A)
_SfpConfigSonetCompliance_Type=Integer32
_SfpConfigSonetCompliance_Object=MibTableColumn
sfpConfigSonetCompliance=_SfpConfigSonetCompliance_Object((1,3,6,1,4,1,4515,1,10,1,1,1,8),_SfpConfigSonetCompliance_Type())
sfpConfigSonetCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigSonetCompliance.setStatus(_A)
_SfpConfigGbeCompliance_Type=Integer32
_SfpConfigGbeCompliance_Object=MibTableColumn
sfpConfigGbeCompliance=_SfpConfigGbeCompliance_Object((1,3,6,1,4,1,4515,1,10,1,1,1,9),_SfpConfigGbeCompliance_Type())
sfpConfigGbeCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigGbeCompliance.setStatus(_A)
_SfpConfigFcCompliance_Type=Integer32
_SfpConfigFcCompliance_Object=MibTableColumn
sfpConfigFcCompliance=_SfpConfigFcCompliance_Object((1,3,6,1,4,1,4515,1,10,1,1,1,10),_SfpConfigFcCompliance_Type())
sfpConfigFcCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigFcCompliance.setStatus(_A)
class _SfpConfigEncodingCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('encUnspecified',0),('enc8B10B',1),('enc4B5B',2),('encNrz',3),('encManchester',4),('encSonet',5),('enc64B66B',6)))
_SfpConfigEncodingCode_Type.__name__=_D
_SfpConfigEncodingCode_Object=MibTableColumn
sfpConfigEncodingCode=_SfpConfigEncodingCode_Object((1,3,6,1,4,1,4515,1,10,1,1,1,11),_SfpConfigEncodingCode_Type())
sfpConfigEncodingCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigEncodingCode.setStatus(_A)
_SfpConfigNominalBitRate_Type=Integer32
_SfpConfigNominalBitRate_Object=MibTableColumn
sfpConfigNominalBitRate=_SfpConfigNominalBitRate_Object((1,3,6,1,4,1,4515,1,10,1,1,1,12),_SfpConfigNominalBitRate_Type())
sfpConfigNominalBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigNominalBitRate.setStatus(_A)
_SfpConfigLength9mKm_Type=Integer32
_SfpConfigLength9mKm_Object=MibTableColumn
sfpConfigLength9mKm=_SfpConfigLength9mKm_Object((1,3,6,1,4,1,4515,1,10,1,1,1,13),_SfpConfigLength9mKm_Type())
sfpConfigLength9mKm.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigLength9mKm.setStatus(_A)
_SfpConfigLength9m100m_Type=Integer32
_SfpConfigLength9m100m_Object=MibTableColumn
sfpConfigLength9m100m=_SfpConfigLength9m100m_Object((1,3,6,1,4,1,4515,1,10,1,1,1,14),_SfpConfigLength9m100m_Type())
sfpConfigLength9m100m.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigLength9m100m.setStatus(_A)
_SfpConfigLength50m10m_Type=Integer32
_SfpConfigLength50m10m_Object=MibTableColumn
sfpConfigLength50m10m=_SfpConfigLength50m10m_Object((1,3,6,1,4,1,4515,1,10,1,1,1,15),_SfpConfigLength50m10m_Type())
sfpConfigLength50m10m.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigLength50m10m.setStatus(_A)
_SfpConfigLength62m10m_Type=Integer32
_SfpConfigLength62m10m_Object=MibTableColumn
sfpConfigLength62m10m=_SfpConfigLength62m10m_Object((1,3,6,1,4,1,4515,1,10,1,1,1,16),_SfpConfigLength62m10m_Type())
sfpConfigLength62m10m.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigLength62m10m.setStatus(_A)
_SfpConfigLengthCopper1m_Type=Integer32
_SfpConfigLengthCopper1m_Object=MibTableColumn
sfpConfigLengthCopper1m=_SfpConfigLengthCopper1m_Object((1,3,6,1,4,1,4515,1,10,1,1,1,17),_SfpConfigLengthCopper1m_Type())
sfpConfigLengthCopper1m.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigLengthCopper1m.setStatus(_A)
_SfpConfigMaxTemp_Type=Integer32
_SfpConfigMaxTemp_Object=MibTableColumn
sfpConfigMaxTemp=_SfpConfigMaxTemp_Object((1,3,6,1,4,1,4515,1,10,1,1,1,18),_SfpConfigMaxTemp_Type())
sfpConfigMaxTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigMaxTemp.setStatus(_A)
_SfpConfigMinTemp_Type=Integer32
_SfpConfigMinTemp_Object=MibTableColumn
sfpConfigMinTemp=_SfpConfigMinTemp_Object((1,3,6,1,4,1,4515,1,10,1,1,1,19),_SfpConfigMinTemp_Type())
sfpConfigMinTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigMinTemp.setStatus(_A)
_SfpConfigMaxSupplyCurrent_Type=Integer32
_SfpConfigMaxSupplyCurrent_Object=MibTableColumn
sfpConfigMaxSupplyCurrent=_SfpConfigMaxSupplyCurrent_Object((1,3,6,1,4,1,4515,1,10,1,1,1,20),_SfpConfigMaxSupplyCurrent_Type())
sfpConfigMaxSupplyCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigMaxSupplyCurrent.setStatus(_A)
_SfpConfigChannelSpacing_Type=Integer32
_SfpConfigChannelSpacing_Object=MibTableColumn
sfpConfigChannelSpacing=_SfpConfigChannelSpacing_Object((1,3,6,1,4,1,4515,1,10,1,1,1,21),_SfpConfigChannelSpacing_Type())
sfpConfigChannelSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigChannelSpacing.setStatus(_A)
class _SfpConfigVendorName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SfpConfigVendorName_Type.__name__=_E
_SfpConfigVendorName_Object=MibTableColumn
sfpConfigVendorName=_SfpConfigVendorName_Object((1,3,6,1,4,1,4515,1,10,1,1,1,22),_SfpConfigVendorName_Type())
sfpConfigVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigVendorName.setStatus(_A)
_SfpConfigOptionalWdm_Type=Integer32
_SfpConfigOptionalWdm_Object=MibTableColumn
sfpConfigOptionalWdm=_SfpConfigOptionalWdm_Object((1,3,6,1,4,1,4515,1,10,1,1,1,23),_SfpConfigOptionalWdm_Type())
sfpConfigOptionalWdm.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigOptionalWdm.setStatus(_A)
_SfpConfigVendorOUI_Type=Integer32
_SfpConfigVendorOUI_Object=MibTableColumn
sfpConfigVendorOUI=_SfpConfigVendorOUI_Object((1,3,6,1,4,1,4515,1,10,1,1,1,24),_SfpConfigVendorOUI_Type())
sfpConfigVendorOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigVendorOUI.setStatus(_A)
class _SfpConfigVendorPN_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SfpConfigVendorPN_Type.__name__=_E
_SfpConfigVendorPN_Object=MibTableColumn
sfpConfigVendorPN=_SfpConfigVendorPN_Object((1,3,6,1,4,1,4515,1,10,1,1,1,25),_SfpConfigVendorPN_Type())
sfpConfigVendorPN.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigVendorPN.setStatus(_A)
class _SfpConfigVendorRev_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_SfpConfigVendorRev_Type.__name__=_E
_SfpConfigVendorRev_Object=MibTableColumn
sfpConfigVendorRev=_SfpConfigVendorRev_Object((1,3,6,1,4,1,4515,1,10,1,1,1,26),_SfpConfigVendorRev_Type())
sfpConfigVendorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigVendorRev.setStatus(_A)
_SfpConfigWaveLength_Type=Integer32
_SfpConfigWaveLength_Object=MibTableColumn
sfpConfigWaveLength=_SfpConfigWaveLength_Object((1,3,6,1,4,1,4515,1,10,1,1,1,27),_SfpConfigWaveLength_Type())
sfpConfigWaveLength.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigWaveLength.setStatus(_A)
_SfpConfigExtendedOptions_Type=Integer32
_SfpConfigExtendedOptions_Object=MibTableColumn
sfpConfigExtendedOptions=_SfpConfigExtendedOptions_Object((1,3,6,1,4,1,4515,1,10,1,1,1,28),_SfpConfigExtendedOptions_Type())
sfpConfigExtendedOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigExtendedOptions.setStatus(_A)
_SfpConfigMaxBitRate_Type=Integer32
_SfpConfigMaxBitRate_Object=MibTableColumn
sfpConfigMaxBitRate=_SfpConfigMaxBitRate_Object((1,3,6,1,4,1,4515,1,10,1,1,1,29),_SfpConfigMaxBitRate_Type())
sfpConfigMaxBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigMaxBitRate.setStatus(_A)
_SfpConfigMinBitRate_Type=Integer32
_SfpConfigMinBitRate_Object=MibTableColumn
sfpConfigMinBitRate=_SfpConfigMinBitRate_Object((1,3,6,1,4,1,4515,1,10,1,1,1,30),_SfpConfigMinBitRate_Type())
sfpConfigMinBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigMinBitRate.setStatus(_A)
class _SfpConfigVendorSN_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SfpConfigVendorSN_Type.__name__=_E
_SfpConfigVendorSN_Object=MibTableColumn
sfpConfigVendorSN=_SfpConfigVendorSN_Object((1,3,6,1,4,1,4515,1,10,1,1,1,31),_SfpConfigVendorSN_Type())
sfpConfigVendorSN.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigVendorSN.setStatus(_A)
class _SfpConfigDateCode_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SfpConfigDateCode_Type.__name__=_E
_SfpConfigDateCode_Object=MibTableColumn
sfpConfigDateCode=_SfpConfigDateCode_Object((1,3,6,1,4,1,4515,1,10,1,1,1,32),_SfpConfigDateCode_Type())
sfpConfigDateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigDateCode.setStatus(_A)
_SfpConfigDiagnosticMonitoring_Type=Integer32
_SfpConfigDiagnosticMonitoring_Object=MibTableColumn
sfpConfigDiagnosticMonitoring=_SfpConfigDiagnosticMonitoring_Object((1,3,6,1,4,1,4515,1,10,1,1,1,33),_SfpConfigDiagnosticMonitoring_Type())
sfpConfigDiagnosticMonitoring.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigDiagnosticMonitoring.setStatus(_A)
_SfpConfigEnhanceOptions_Type=Integer32
_SfpConfigEnhanceOptions_Object=MibTableColumn
sfpConfigEnhanceOptions=_SfpConfigEnhanceOptions_Object((1,3,6,1,4,1,4515,1,10,1,1,1,34),_SfpConfigEnhanceOptions_Type())
sfpConfigEnhanceOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigEnhanceOptions.setStatus(_A)
class _SfpConfig8472Compliance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noDiag',0),('rev93',1),('rev94',2)))
_SfpConfig8472Compliance_Type.__name__=_D
_SfpConfig8472Compliance_Object=MibTableColumn
sfpConfig8472Compliance=_SfpConfig8472Compliance_Object((1,3,6,1,4,1,4515,1,10,1,1,1,35),_SfpConfig8472Compliance_Type())
sfpConfig8472Compliance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfig8472Compliance.setStatus(_A)
_SfpConfigTunableWaveLength_Type=Integer32
_SfpConfigTunableWaveLength_Object=MibTableColumn
sfpConfigTunableWaveLength=_SfpConfigTunableWaveLength_Object((1,3,6,1,4,1,4515,1,10,1,1,1,36),_SfpConfigTunableWaveLength_Type())
sfpConfigTunableWaveLength.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigTunableWaveLength.setStatus(_A)
_SfpConfigVoaControl_Type=Integer32
_SfpConfigVoaControl_Object=MibTableColumn
sfpConfigVoaControl=_SfpConfigVoaControl_Object((1,3,6,1,4,1,4515,1,10,1,1,1,37),_SfpConfigVoaControl_Type())
sfpConfigVoaControl.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigVoaControl.setStatus(_A)
_SfpConfigVdtControl_Type=Integer32
_SfpConfigVdtControl_Object=MibTableColumn
sfpConfigVdtControl=_SfpConfigVdtControl_Object((1,3,6,1,4,1,4515,1,10,1,1,1,38),_SfpConfigVdtControl_Type())
sfpConfigVdtControl.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigVdtControl.setStatus(_A)
_SfpConfigPilotToneModulation_Type=Integer32
_SfpConfigPilotToneModulation_Object=MibTableColumn
sfpConfigPilotToneModulation=_SfpConfigPilotToneModulation_Object((1,3,6,1,4,1,4515,1,10,1,1,1,39),_SfpConfigPilotToneModulation_Type())
sfpConfigPilotToneModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigPilotToneModulation.setStatus(_A)
class _SfpConfigCleiCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_SfpConfigCleiCode_Type.__name__=_H
_SfpConfigCleiCode_Object=MibTableColumn
sfpConfigCleiCode=_SfpConfigCleiCode_Object((1,3,6,1,4,1,4515,1,10,1,1,1,40),_SfpConfigCleiCode_Type())
sfpConfigCleiCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCleiCode.setStatus(_A)
_SfpConfigXfpExtXcvrId_Type=Integer32
_SfpConfigXfpExtXcvrId_Object=MibTableColumn
sfpConfigXfpExtXcvrId=_SfpConfigXfpExtXcvrId_Object((1,3,6,1,4,1,4515,1,10,1,1,1,41),_SfpConfigXfpExtXcvrId_Type())
sfpConfigXfpExtXcvrId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpExtXcvrId.setStatus(_A)
_SfpConfigXfpEncodingCode_Type=Integer32
_SfpConfigXfpEncodingCode_Object=MibTableColumn
sfpConfigXfpEncodingCode=_SfpConfigXfpEncodingCode_Object((1,3,6,1,4,1,4515,1,10,1,1,1,42),_SfpConfigXfpEncodingCode_Type())
sfpConfigXfpEncodingCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpEncodingCode.setStatus(_A)
_SfpConfigXfpMinBitRate_Type=Integer32
_SfpConfigXfpMinBitRate_Object=MibTableColumn
sfpConfigXfpMinBitRate=_SfpConfigXfpMinBitRate_Object((1,3,6,1,4,1,4515,1,10,1,1,1,43),_SfpConfigXfpMinBitRate_Type())
sfpConfigXfpMinBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpMinBitRate.setStatus(_A)
_SfpConfigXfpMaxBitRate_Type=Integer32
_SfpConfigXfpMaxBitRate_Object=MibTableColumn
sfpConfigXfpMaxBitRate=_SfpConfigXfpMaxBitRate_Object((1,3,6,1,4,1,4515,1,10,1,1,1,44),_SfpConfigXfpMaxBitRate_Type())
sfpConfigXfpMaxBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpMaxBitRate.setStatus(_A)
_SfpConfig10GSonetCompliance_Type=Integer32
_SfpConfig10GSonetCompliance_Object=MibTableColumn
sfpConfig10GSonetCompliance=_SfpConfig10GSonetCompliance_Object((1,3,6,1,4,1,4515,1,10,1,1,1,45),_SfpConfig10GSonetCompliance_Type())
sfpConfig10GSonetCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfig10GSonetCompliance.setStatus(_A)
_SfpConfig10GbeCompliance_Type=Integer32
_SfpConfig10GbeCompliance_Object=MibTableColumn
sfpConfig10GbeCompliance=_SfpConfig10GbeCompliance_Object((1,3,6,1,4,1,4515,1,10,1,1,1,46),_SfpConfig10GbeCompliance_Type())
sfpConfig10GbeCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfig10GbeCompliance.setStatus(_A)
_SfpConfig10GFcCompliance_Type=Integer32
_SfpConfig10GFcCompliance_Object=MibTableColumn
sfpConfig10GFcCompliance=_SfpConfig10GFcCompliance_Object((1,3,6,1,4,1,4515,1,10,1,1,1,47),_SfpConfig10GFcCompliance_Type())
sfpConfig10GFcCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfig10GFcCompliance.setStatus(_A)
_SfpConfigXfpDeviceTech_Type=Integer32
_SfpConfigXfpDeviceTech_Object=MibTableColumn
sfpConfigXfpDeviceTech=_SfpConfigXfpDeviceTech_Object((1,3,6,1,4,1,4515,1,10,1,1,1,48),_SfpConfigXfpDeviceTech_Type())
sfpConfigXfpDeviceTech.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpDeviceTech.setStatus(_A)
_SfpConfigXfpTuningSupported_Type=Integer32
_SfpConfigXfpTuningSupported_Object=MibTableColumn
sfpConfigXfpTuningSupported=_SfpConfigXfpTuningSupported_Object((1,3,6,1,4,1,4515,1,10,1,1,1,49),_SfpConfigXfpTuningSupported_Type())
sfpConfigXfpTuningSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpTuningSupported.setStatus(_A)
_SfpConfigXfpDesiredChannel_Type=Integer32
_SfpConfigXfpDesiredChannel_Object=MibTableColumn
sfpConfigXfpDesiredChannel=_SfpConfigXfpDesiredChannel_Object((1,3,6,1,4,1,4515,1,10,1,1,1,50),_SfpConfigXfpDesiredChannel_Type())
sfpConfigXfpDesiredChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigXfpDesiredChannel.setStatus(_A)
_SfpConfigXfpDesiredWl_Type=Integer32
_SfpConfigXfpDesiredWl_Object=MibTableColumn
sfpConfigXfpDesiredWl=_SfpConfigXfpDesiredWl_Object((1,3,6,1,4,1,4515,1,10,1,1,1,51),_SfpConfigXfpDesiredWl_Type())
sfpConfigXfpDesiredWl.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigXfpDesiredWl.setStatus(_A)
_SfpConfigXfpWlError_Type=Integer32
_SfpConfigXfpWlError_Object=MibTableColumn
sfpConfigXfpWlError=_SfpConfigXfpWlError_Object((1,3,6,1,4,1,4515,1,10,1,1,1,52),_SfpConfigXfpWlError_Type())
sfpConfigXfpWlError.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpWlError.setStatus(_A)
_SfpConfigXfpDesiredFreq_Type=Integer32
_SfpConfigXfpDesiredFreq_Object=MibTableColumn
sfpConfigXfpDesiredFreq=_SfpConfigXfpDesiredFreq_Object((1,3,6,1,4,1,4515,1,10,1,1,1,53),_SfpConfigXfpDesiredFreq_Type())
sfpConfigXfpDesiredFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigXfpDesiredFreq.setStatus(_A)
_SfpConfigXfpFreqError_Type=Integer32
_SfpConfigXfpFreqError_Object=MibTableColumn
sfpConfigXfpFreqError=_SfpConfigXfpFreqError_Object((1,3,6,1,4,1,4515,1,10,1,1,1,54),_SfpConfigXfpFreqError_Type())
sfpConfigXfpFreqError.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpFreqError.setStatus(_A)
_SfpConfigXfpDitherSupported_Type=TruthValue
_SfpConfigXfpDitherSupported_Object=MibTableColumn
sfpConfigXfpDitherSupported=_SfpConfigXfpDitherSupported_Object((1,3,6,1,4,1,4515,1,10,1,1,1,55),_SfpConfigXfpDitherSupported_Type())
sfpConfigXfpDitherSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpDitherSupported.setStatus(_A)
class _SfpConfigXfpDitherAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_SfpConfigXfpDitherAdmin_Type.__name__=_D
_SfpConfigXfpDitherAdmin_Object=MibTableColumn
sfpConfigXfpDitherAdmin=_SfpConfigXfpDitherAdmin_Object((1,3,6,1,4,1,4515,1,10,1,1,1,56),_SfpConfigXfpDitherAdmin_Type())
sfpConfigXfpDitherAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigXfpDitherAdmin.setStatus(_A)
_SfpConfigXfpCapFreqFirstThz_Type=Integer32
_SfpConfigXfpCapFreqFirstThz_Object=MibTableColumn
sfpConfigXfpCapFreqFirstThz=_SfpConfigXfpCapFreqFirstThz_Object((1,3,6,1,4,1,4515,1,10,1,1,1,57),_SfpConfigXfpCapFreqFirstThz_Type())
sfpConfigXfpCapFreqFirstThz.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpCapFreqFirstThz.setStatus(_A)
_SfpConfigXfpCapFreqFirst10Ghz_Type=Integer32
_SfpConfigXfpCapFreqFirst10Ghz_Object=MibTableColumn
sfpConfigXfpCapFreqFirst10Ghz=_SfpConfigXfpCapFreqFirst10Ghz_Object((1,3,6,1,4,1,4515,1,10,1,1,1,58),_SfpConfigXfpCapFreqFirst10Ghz_Type())
sfpConfigXfpCapFreqFirst10Ghz.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpCapFreqFirst10Ghz.setStatus(_A)
_SfpConfigXfpCapFreqLastThz_Type=Integer32
_SfpConfigXfpCapFreqLastThz_Object=MibTableColumn
sfpConfigXfpCapFreqLastThz=_SfpConfigXfpCapFreqLastThz_Object((1,3,6,1,4,1,4515,1,10,1,1,1,59),_SfpConfigXfpCapFreqLastThz_Type())
sfpConfigXfpCapFreqLastThz.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpCapFreqLastThz.setStatus(_A)
_SfpConfigXfpCapFreqLast10Ghz_Type=Integer32
_SfpConfigXfpCapFreqLast10Ghz_Object=MibTableColumn
sfpConfigXfpCapFreqLast10Ghz=_SfpConfigXfpCapFreqLast10Ghz_Object((1,3,6,1,4,1,4515,1,10,1,1,1,60),_SfpConfigXfpCapFreqLast10Ghz_Type())
sfpConfigXfpCapFreqLast10Ghz.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpCapFreqLast10Ghz.setStatus(_A)
_SfpConfigXfpCapMaxSpacing10Ghz_Type=Integer32
_SfpConfigXfpCapMaxSpacing10Ghz_Object=MibTableColumn
sfpConfigXfpCapMaxSpacing10Ghz=_SfpConfigXfpCapMaxSpacing10Ghz_Object((1,3,6,1,4,1,4515,1,10,1,1,1,61),_SfpConfigXfpCapMaxSpacing10Ghz_Type())
sfpConfigXfpCapMaxSpacing10Ghz.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpCapMaxSpacing10Ghz.setStatus(_A)
_SfpConfigXfpCalibrationSupported_Type=TruthValue
_SfpConfigXfpCalibrationSupported_Object=MibTableColumn
sfpConfigXfpCalibrationSupported=_SfpConfigXfpCalibrationSupported_Object((1,3,6,1,4,1,4515,1,10,1,1,1,62),_SfpConfigXfpCalibrationSupported_Type())
sfpConfigXfpCalibrationSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigXfpCalibrationSupported.setStatus(_A)
_SfpConfigXfpCalibrationEnabled_Type=TruthValue
_SfpConfigXfpCalibrationEnabled_Object=MibTableColumn
sfpConfigXfpCalibrationEnabled=_SfpConfigXfpCalibrationEnabled_Object((1,3,6,1,4,1,4515,1,10,1,1,1,63),_SfpConfigXfpCalibrationEnabled_Type())
sfpConfigXfpCalibrationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigXfpCalibrationEnabled.setStatus(_A)
_SfpConfigCfpExtId_Type=Integer32
_SfpConfigCfpExtId_Object=MibTableColumn
sfpConfigCfpExtId=_SfpConfigCfpExtId_Object((1,3,6,1,4,1,4515,1,10,1,1,1,70),_SfpConfigCfpExtId_Type())
sfpConfigCfpExtId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpExtId.setStatus(_A)
_SfpConfigCfpConnectorType_Type=Integer32
_SfpConfigCfpConnectorType_Object=MibTableColumn
sfpConfigCfpConnectorType=_SfpConfigCfpConnectorType_Object((1,3,6,1,4,1,4515,1,10,1,1,1,71),_SfpConfigCfpConnectorType_Type())
sfpConfigCfpConnectorType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpConnectorType.setStatus(_A)
_SfpConfigCfpEthernetCode_Type=Integer32
_SfpConfigCfpEthernetCode_Object=MibTableColumn
sfpConfigCfpEthernetCode=_SfpConfigCfpEthernetCode_Object((1,3,6,1,4,1,4515,1,10,1,1,1,72),_SfpConfigCfpEthernetCode_Type())
sfpConfigCfpEthernetCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpEthernetCode.setStatus(_A)
_SfpConfigCfpFcCode_Type=Integer32
_SfpConfigCfpFcCode_Object=MibTableColumn
sfpConfigCfpFcCode=_SfpConfigCfpFcCode_Object((1,3,6,1,4,1,4515,1,10,1,1,1,73),_SfpConfigCfpFcCode_Type())
sfpConfigCfpFcCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpFcCode.setStatus(_A)
_SfpConfigCfpCopperCode_Type=Integer32
_SfpConfigCfpCopperCode_Object=MibTableColumn
sfpConfigCfpCopperCode=_SfpConfigCfpCopperCode_Object((1,3,6,1,4,1,4515,1,10,1,1,1,74),_SfpConfigCfpCopperCode_Type())
sfpConfigCfpCopperCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpCopperCode.setStatus(_A)
_SfpConfigCfpSonetCode_Type=Integer32
_SfpConfigCfpSonetCode_Object=MibTableColumn
sfpConfigCfpSonetCode=_SfpConfigCfpSonetCode_Object((1,3,6,1,4,1,4515,1,10,1,1,1,75),_SfpConfigCfpSonetCode_Type())
sfpConfigCfpSonetCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpSonetCode.setStatus(_A)
_SfpConfigCfpOtnCode_Type=Integer32
_SfpConfigCfpOtnCode_Object=MibTableColumn
sfpConfigCfpOtnCode=_SfpConfigCfpOtnCode_Object((1,3,6,1,4,1,4515,1,10,1,1,1,76),_SfpConfigCfpOtnCode_Type())
sfpConfigCfpOtnCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpOtnCode.setStatus(_A)
_SfpConfigCfpSupportedRates_Type=Integer32
_SfpConfigCfpSupportedRates_Object=MibTableColumn
sfpConfigCfpSupportedRates=_SfpConfigCfpSupportedRates_Object((1,3,6,1,4,1,4515,1,10,1,1,1,77),_SfpConfigCfpSupportedRates_Type())
sfpConfigCfpSupportedRates.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpSupportedRates.setStatus(_A)
_SfpConfigCfpSupportedLanes_Type=Integer32
_SfpConfigCfpSupportedLanes_Object=MibTableColumn
sfpConfigCfpSupportedLanes=_SfpConfigCfpSupportedLanes_Object((1,3,6,1,4,1,4515,1,10,1,1,1,78),_SfpConfigCfpSupportedLanes_Type())
sfpConfigCfpSupportedLanes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpSupportedLanes.setStatus(_A)
_SfpConfigCfpMediaProperties_Type=Integer32
_SfpConfigCfpMediaProperties_Object=MibTableColumn
sfpConfigCfpMediaProperties=_SfpConfigCfpMediaProperties_Object((1,3,6,1,4,1,4515,1,10,1,1,1,79),_SfpConfigCfpMediaProperties_Type())
sfpConfigCfpMediaProperties.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpMediaProperties.setStatus(_A)
_SfpConfigCfpMaxNetworkLaneRate_Type=Integer32
_SfpConfigCfpMaxNetworkLaneRate_Object=MibTableColumn
sfpConfigCfpMaxNetworkLaneRate=_SfpConfigCfpMaxNetworkLaneRate_Object((1,3,6,1,4,1,4515,1,10,1,1,1,80),_SfpConfigCfpMaxNetworkLaneRate_Type())
sfpConfigCfpMaxNetworkLaneRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpMaxNetworkLaneRate.setStatus(_A)
_SfpConfigCfpMaxHostLaneRate_Type=Integer32
_SfpConfigCfpMaxHostLaneRate_Object=MibTableColumn
sfpConfigCfpMaxHostLaneRate=_SfpConfigCfpMaxHostLaneRate_Object((1,3,6,1,4,1,4515,1,10,1,1,1,81),_SfpConfigCfpMaxHostLaneRate_Type())
sfpConfigCfpMaxHostLaneRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpMaxHostLaneRate.setStatus(_A)
_SfpConfigCfpMaxSmFiberLength_Type=Integer32
_SfpConfigCfpMaxSmFiberLength_Object=MibTableColumn
sfpConfigCfpMaxSmFiberLength=_SfpConfigCfpMaxSmFiberLength_Object((1,3,6,1,4,1,4515,1,10,1,1,1,82),_SfpConfigCfpMaxSmFiberLength_Type())
sfpConfigCfpMaxSmFiberLength.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpMaxSmFiberLength.setStatus(_A)
_SfpConfigCfpMaxMmFiberLength_Type=Integer32
_SfpConfigCfpMaxMmFiberLength_Object=MibTableColumn
sfpConfigCfpMaxMmFiberLength=_SfpConfigCfpMaxMmFiberLength_Object((1,3,6,1,4,1,4515,1,10,1,1,1,83),_SfpConfigCfpMaxMmFiberLength_Type())
sfpConfigCfpMaxMmFiberLength.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpMaxMmFiberLength.setStatus(_A)
_SfpConfigCfpMaxCopperCableLength_Type=Integer32
_SfpConfigCfpMaxCopperCableLength_Object=MibTableColumn
sfpConfigCfpMaxCopperCableLength=_SfpConfigCfpMaxCopperCableLength_Object((1,3,6,1,4,1,4515,1,10,1,1,1,84),_SfpConfigCfpMaxCopperCableLength_Type())
sfpConfigCfpMaxCopperCableLength.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpMaxCopperCableLength.setStatus(_A)
_SfpConfigCfpMinWavelenPerActive_Type=Integer32
_SfpConfigCfpMinWavelenPerActive_Object=MibTableColumn
sfpConfigCfpMinWavelenPerActive=_SfpConfigCfpMinWavelenPerActive_Object((1,3,6,1,4,1,4515,1,10,1,1,1,85),_SfpConfigCfpMinWavelenPerActive_Type())
sfpConfigCfpMinWavelenPerActive.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpMinWavelenPerActive.setStatus(_A)
_SfpConfigCfpMaxWavelenPerActive_Type=Integer32
_SfpConfigCfpMaxWavelenPerActive_Object=MibTableColumn
sfpConfigCfpMaxWavelenPerActive=_SfpConfigCfpMaxWavelenPerActive_Object((1,3,6,1,4,1,4515,1,10,1,1,1,86),_SfpConfigCfpMaxWavelenPerActive_Type())
sfpConfigCfpMaxWavelenPerActive.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpMaxWavelenPerActive.setStatus(_A)
_SfpConfigCfpMaxLenOpticalWidth_Type=Integer32
_SfpConfigCfpMaxLenOpticalWidth_Object=MibTableColumn
sfpConfigCfpMaxLenOpticalWidth=_SfpConfigCfpMaxLenOpticalWidth_Object((1,3,6,1,4,1,4515,1,10,1,1,1,87),_SfpConfigCfpMaxLenOpticalWidth_Type())
sfpConfigCfpMaxLenOpticalWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCfpMaxLenOpticalWidth.setStatus(_A)
_SfpConfigCfpSpacing_Type=Integer32
_SfpConfigCfpSpacing_Object=MibTableColumn
sfpConfigCfpSpacing=_SfpConfigCfpSpacing_Object((1,3,6,1,4,1,4515,1,10,1,1,1,88),_SfpConfigCfpSpacing_Type())
sfpConfigCfpSpacing.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigCfpSpacing.setStatus(_A)
_SfpConfigQsfppEthernetCode_Type=Integer32
_SfpConfigQsfppEthernetCode_Object=MibTableColumn
sfpConfigQsfppEthernetCode=_SfpConfigQsfppEthernetCode_Object((1,3,6,1,4,1,4515,1,10,1,1,1,100),_SfpConfigQsfppEthernetCode_Type())
sfpConfigQsfppEthernetCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigQsfppEthernetCode.setStatus(_A)
_SfpConfigQsfppSonetCode_Type=Integer32
_SfpConfigQsfppSonetCode_Object=MibTableColumn
sfpConfigQsfppSonetCode=_SfpConfigQsfppSonetCode_Object((1,3,6,1,4,1,4515,1,10,1,1,1,101),_SfpConfigQsfppSonetCode_Type())
sfpConfigQsfppSonetCode.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigQsfppSonetCode.setStatus(_A)
_SfpConfigCxpExtId_Type=Integer32
_SfpConfigCxpExtId_Object=MibTableColumn
sfpConfigCxpExtId=_SfpConfigCxpExtId_Object((1,3,6,1,4,1,4515,1,10,1,1,1,110),_SfpConfigCxpExtId_Type())
sfpConfigCxpExtId.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigCxpExtId.setStatus(_A)
_SfpConfigCxpConnectorType_Type=Integer32
_SfpConfigCxpConnectorType_Object=MibTableColumn
sfpConfigCxpConnectorType=_SfpConfigCxpConnectorType_Object((1,3,6,1,4,1,4515,1,10,1,1,1,111),_SfpConfigCxpConnectorType_Type())
sfpConfigCxpConnectorType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigCxpConnectorType.setStatus(_A)
_SfpConfigCxpMaxSupportedRate_Type=Integer32
_SfpConfigCxpMaxSupportedRate_Object=MibTableColumn
sfpConfigCxpMaxSupportedRate=_SfpConfigCxpMaxSupportedRate_Object((1,3,6,1,4,1,4515,1,10,1,1,1,112),_SfpConfigCxpMaxSupportedRate_Type())
sfpConfigCxpMaxSupportedRate.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigCxpMaxSupportedRate.setStatus(_A)
_SfpConfigCxpNominalWavelength_Type=Integer32
_SfpConfigCxpNominalWavelength_Object=MibTableColumn
sfpConfigCxpNominalWavelength=_SfpConfigCxpNominalWavelength_Object((1,3,6,1,4,1,4515,1,10,1,1,1,113),_SfpConfigCxpNominalWavelength_Type())
sfpConfigCxpNominalWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigCxpNominalWavelength.setStatus(_A)
_SfpConfigCxpDeviceTech_Type=Integer32
_SfpConfigCxpDeviceTech_Object=MibTableColumn
sfpConfigCxpDeviceTech=_SfpConfigCxpDeviceTech_Object((1,3,6,1,4,1,4515,1,10,1,1,1,114),_SfpConfigCxpDeviceTech_Type())
sfpConfigCxpDeviceTech.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigCxpDeviceTech.setStatus(_A)
_SfpConfigCohRxDesiredChannel_Type=Integer32
_SfpConfigCohRxDesiredChannel_Object=MibTableColumn
sfpConfigCohRxDesiredChannel=_SfpConfigCohRxDesiredChannel_Object((1,3,6,1,4,1,4515,1,10,1,1,1,115),_SfpConfigCohRxDesiredChannel_Type())
sfpConfigCohRxDesiredChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigCohRxDesiredChannel.setStatus(_A)
_SfpConfigCohRxDesiredWl_Type=Integer32
_SfpConfigCohRxDesiredWl_Object=MibTableColumn
sfpConfigCohRxDesiredWl=_SfpConfigCohRxDesiredWl_Object((1,3,6,1,4,1,4515,1,10,1,1,1,116),_SfpConfigCohRxDesiredWl_Type())
sfpConfigCohRxDesiredWl.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigCohRxDesiredWl.setStatus(_A)
_SfpConfigCohRxDesiredFreq_Type=Integer32
_SfpConfigCohRxDesiredFreq_Object=MibTableColumn
sfpConfigCohRxDesiredFreq=_SfpConfigCohRxDesiredFreq_Object((1,3,6,1,4,1,4515,1,10,1,1,1,117),_SfpConfigCohRxDesiredFreq_Type())
sfpConfigCohRxDesiredFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigCohRxDesiredFreq.setStatus(_A)
_SfpConfigCohCurrentCD_Type=Integer32
_SfpConfigCohCurrentCD_Object=MibTableColumn
sfpConfigCohCurrentCD=_SfpConfigCohCurrentCD_Object((1,3,6,1,4,1,4515,1,10,1,1,1,118),_SfpConfigCohCurrentCD_Type())
sfpConfigCohCurrentCD.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCohCurrentCD.setStatus(_A)
_SfpConfigCohCurrentOSNR_Type=Integer32
_SfpConfigCohCurrentOSNR_Object=MibTableColumn
sfpConfigCohCurrentOSNR=_SfpConfigCohCurrentOSNR_Object((1,3,6,1,4,1,4515,1,10,1,1,1,119),_SfpConfigCohCurrentOSNR_Type())
sfpConfigCohCurrentOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCohCurrentOSNR.setStatus(_A)
_SfpConfigCohAverageOSNR_Type=Integer32
_SfpConfigCohAverageOSNR_Object=MibTableColumn
sfpConfigCohAverageOSNR=_SfpConfigCohAverageOSNR_Object((1,3,6,1,4,1,4515,1,10,1,1,1,120),_SfpConfigCohAverageOSNR_Type())
sfpConfigCohAverageOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCohAverageOSNR.setStatus(_A)
_SfpConfigCohMaxCD_Type=Integer32
_SfpConfigCohMaxCD_Object=MibTableColumn
sfpConfigCohMaxCD=_SfpConfigCohMaxCD_Object((1,3,6,1,4,1,4515,1,10,1,1,1,121),_SfpConfigCohMaxCD_Type())
sfpConfigCohMaxCD.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConfigCohMaxCD.setStatus(_A)
_SfpConfigNyquist_Type=TruthValue
_SfpConfigNyquist_Object=MibTableColumn
sfpConfigNyquist=_SfpConfigNyquist_Object((1,3,6,1,4,1,4515,1,10,1,1,1,122),_SfpConfigNyquist_Type())
sfpConfigNyquist.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigNyquist.setStatus(_A)
_SfpConfigModulationFormat_Type=Integer32
_SfpConfigModulationFormat_Object=MibTableColumn
sfpConfigModulationFormat=_SfpConfigModulationFormat_Object((1,3,6,1,4,1,4515,1,10,1,1,1,123),_SfpConfigModulationFormat_Type())
sfpConfigModulationFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConfigModulationFormat.setStatus(_A)
_SfpDiag_ObjectIdentity=ObjectIdentity
sfpDiag=_SfpDiag_ObjectIdentity((1,3,6,1,4,1,4515,1,10,2))
_SfpDiagTable_Object=MibTable
sfpDiagTable=_SfpDiagTable_Object((1,3,6,1,4,1,4515,1,10,2,1))
if mibBuilder.loadTexts:sfpDiagTable.setStatus(_A)
_SfpDiagEntry_Object=MibTableRow
sfpDiagEntry=_SfpDiagEntry_Object((1,3,6,1,4,1,4515,1,10,2,1,1))
sfpDiagEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:sfpDiagEntry.setStatus(_A)
_SfpDiagInterface_Type=InterfaceIndex
_SfpDiagInterface_Object=MibTableColumn
sfpDiagInterface=_SfpDiagInterface_Object((1,3,6,1,4,1,4515,1,10,2,1,1,1),_SfpDiagInterface_Type())
sfpDiagInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagInterface.setStatus(_A)
class _SfpDiagHighTempAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighTempAlmThreshold_Type.__name__=_D
_SfpDiagHighTempAlmThreshold_Object=MibTableColumn
sfpDiagHighTempAlmThreshold=_SfpDiagHighTempAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,2),_SfpDiagHighTempAlmThreshold_Type())
sfpDiagHighTempAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighTempAlmThreshold.setStatus(_A)
class _SfpDiagLowTempAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowTempAlmThreshold_Type.__name__=_D
_SfpDiagLowTempAlmThreshold_Object=MibTableColumn
sfpDiagLowTempAlmThreshold=_SfpDiagLowTempAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,3),_SfpDiagLowTempAlmThreshold_Type())
sfpDiagLowTempAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowTempAlmThreshold.setStatus(_A)
class _SfpDiagHighTempWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighTempWrnThreshold_Type.__name__=_D
_SfpDiagHighTempWrnThreshold_Object=MibTableColumn
sfpDiagHighTempWrnThreshold=_SfpDiagHighTempWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,4),_SfpDiagHighTempWrnThreshold_Type())
sfpDiagHighTempWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighTempWrnThreshold.setStatus(_A)
class _SfpDiagLowTempWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowTempWrnThreshold_Type.__name__=_D
_SfpDiagLowTempWrnThreshold_Object=MibTableColumn
sfpDiagLowTempWrnThreshold=_SfpDiagLowTempWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,5),_SfpDiagLowTempWrnThreshold_Type())
sfpDiagLowTempWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowTempWrnThreshold.setStatus(_A)
class _SfpDiagHighVoltAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighVoltAlmThreshold_Type.__name__=_D
_SfpDiagHighVoltAlmThreshold_Object=MibTableColumn
sfpDiagHighVoltAlmThreshold=_SfpDiagHighVoltAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,6),_SfpDiagHighVoltAlmThreshold_Type())
sfpDiagHighVoltAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighVoltAlmThreshold.setStatus(_A)
class _SfpDiagLowVoltAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowVoltAlmThreshold_Type.__name__=_D
_SfpDiagLowVoltAlmThreshold_Object=MibTableColumn
sfpDiagLowVoltAlmThreshold=_SfpDiagLowVoltAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,7),_SfpDiagLowVoltAlmThreshold_Type())
sfpDiagLowVoltAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowVoltAlmThreshold.setStatus(_A)
class _SfpDiagHighVoltWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighVoltWrnThreshold_Type.__name__=_D
_SfpDiagHighVoltWrnThreshold_Object=MibTableColumn
sfpDiagHighVoltWrnThreshold=_SfpDiagHighVoltWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,8),_SfpDiagHighVoltWrnThreshold_Type())
sfpDiagHighVoltWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighVoltWrnThreshold.setStatus(_A)
class _SfpDiagLowVoltWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowVoltWrnThreshold_Type.__name__=_D
_SfpDiagLowVoltWrnThreshold_Object=MibTableColumn
sfpDiagLowVoltWrnThreshold=_SfpDiagLowVoltWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,9),_SfpDiagLowVoltWrnThreshold_Type())
sfpDiagLowVoltWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowVoltWrnThreshold.setStatus(_A)
class _SfpDiagHighTxBiasAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighTxBiasAlmThreshold_Type.__name__=_D
_SfpDiagHighTxBiasAlmThreshold_Object=MibTableColumn
sfpDiagHighTxBiasAlmThreshold=_SfpDiagHighTxBiasAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,10),_SfpDiagHighTxBiasAlmThreshold_Type())
sfpDiagHighTxBiasAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighTxBiasAlmThreshold.setStatus(_A)
class _SfpDiagLowTxBiasAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowTxBiasAlmThreshold_Type.__name__=_D
_SfpDiagLowTxBiasAlmThreshold_Object=MibTableColumn
sfpDiagLowTxBiasAlmThreshold=_SfpDiagLowTxBiasAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,11),_SfpDiagLowTxBiasAlmThreshold_Type())
sfpDiagLowTxBiasAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowTxBiasAlmThreshold.setStatus(_A)
class _SfpDiagHighTxBiasWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighTxBiasWrnThreshold_Type.__name__=_D
_SfpDiagHighTxBiasWrnThreshold_Object=MibTableColumn
sfpDiagHighTxBiasWrnThreshold=_SfpDiagHighTxBiasWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,12),_SfpDiagHighTxBiasWrnThreshold_Type())
sfpDiagHighTxBiasWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighTxBiasWrnThreshold.setStatus(_A)
class _SfpDiagLowTxBiasWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowTxBiasWrnThreshold_Type.__name__=_D
_SfpDiagLowTxBiasWrnThreshold_Object=MibTableColumn
sfpDiagLowTxBiasWrnThreshold=_SfpDiagLowTxBiasWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,13),_SfpDiagLowTxBiasWrnThreshold_Type())
sfpDiagLowTxBiasWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowTxBiasWrnThreshold.setStatus(_A)
class _SfpDiagHighTxPowerAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighTxPowerAlmThreshold_Type.__name__=_D
_SfpDiagHighTxPowerAlmThreshold_Object=MibTableColumn
sfpDiagHighTxPowerAlmThreshold=_SfpDiagHighTxPowerAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,14),_SfpDiagHighTxPowerAlmThreshold_Type())
sfpDiagHighTxPowerAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighTxPowerAlmThreshold.setStatus(_A)
class _SfpDiagLowTxPowerAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowTxPowerAlmThreshold_Type.__name__=_D
_SfpDiagLowTxPowerAlmThreshold_Object=MibTableColumn
sfpDiagLowTxPowerAlmThreshold=_SfpDiagLowTxPowerAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,15),_SfpDiagLowTxPowerAlmThreshold_Type())
sfpDiagLowTxPowerAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowTxPowerAlmThreshold.setStatus(_A)
class _SfpDiagHighTxPowerWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighTxPowerWrnThreshold_Type.__name__=_D
_SfpDiagHighTxPowerWrnThreshold_Object=MibTableColumn
sfpDiagHighTxPowerWrnThreshold=_SfpDiagHighTxPowerWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,16),_SfpDiagHighTxPowerWrnThreshold_Type())
sfpDiagHighTxPowerWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighTxPowerWrnThreshold.setStatus(_A)
class _SfpDiagLowTxPowerWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowTxPowerWrnThreshold_Type.__name__=_D
_SfpDiagLowTxPowerWrnThreshold_Object=MibTableColumn
sfpDiagLowTxPowerWrnThreshold=_SfpDiagLowTxPowerWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,17),_SfpDiagLowTxPowerWrnThreshold_Type())
sfpDiagLowTxPowerWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowTxPowerWrnThreshold.setStatus(_A)
class _SfpDiagHighRxPowerAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighRxPowerAlmThreshold_Type.__name__=_D
_SfpDiagHighRxPowerAlmThreshold_Object=MibTableColumn
sfpDiagHighRxPowerAlmThreshold=_SfpDiagHighRxPowerAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,18),_SfpDiagHighRxPowerAlmThreshold_Type())
sfpDiagHighRxPowerAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighRxPowerAlmThreshold.setStatus(_A)
class _SfpDiagLowRxPowerAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowRxPowerAlmThreshold_Type.__name__=_D
_SfpDiagLowRxPowerAlmThreshold_Object=MibTableColumn
sfpDiagLowRxPowerAlmThreshold=_SfpDiagLowRxPowerAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,19),_SfpDiagLowRxPowerAlmThreshold_Type())
sfpDiagLowRxPowerAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowRxPowerAlmThreshold.setStatus(_A)
class _SfpDiagHighRxPowerWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighRxPowerWrnThreshold_Type.__name__=_D
_SfpDiagHighRxPowerWrnThreshold_Object=MibTableColumn
sfpDiagHighRxPowerWrnThreshold=_SfpDiagHighRxPowerWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,20),_SfpDiagHighRxPowerWrnThreshold_Type())
sfpDiagHighRxPowerWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighRxPowerWrnThreshold.setStatus(_A)
class _SfpDiagLowRxPowerWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowRxPowerWrnThreshold_Type.__name__=_D
_SfpDiagLowRxPowerWrnThreshold_Object=MibTableColumn
sfpDiagLowRxPowerWrnThreshold=_SfpDiagLowRxPowerWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,21),_SfpDiagLowRxPowerWrnThreshold_Type())
sfpDiagLowRxPowerWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowRxPowerWrnThreshold.setStatus(_A)
class _SfpDiagHighLaserTempAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighLaserTempAlmThreshold_Type.__name__=_D
_SfpDiagHighLaserTempAlmThreshold_Object=MibTableColumn
sfpDiagHighLaserTempAlmThreshold=_SfpDiagHighLaserTempAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,22),_SfpDiagHighLaserTempAlmThreshold_Type())
sfpDiagHighLaserTempAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighLaserTempAlmThreshold.setStatus(_A)
class _SfpDiagLowLaserTempAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowLaserTempAlmThreshold_Type.__name__=_D
_SfpDiagLowLaserTempAlmThreshold_Object=MibTableColumn
sfpDiagLowLaserTempAlmThreshold=_SfpDiagLowLaserTempAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,23),_SfpDiagLowLaserTempAlmThreshold_Type())
sfpDiagLowLaserTempAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowLaserTempAlmThreshold.setStatus(_A)
class _SfpDiagHighLaserTempWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighLaserTempWrnThreshold_Type.__name__=_D
_SfpDiagHighLaserTempWrnThreshold_Object=MibTableColumn
sfpDiagHighLaserTempWrnThreshold=_SfpDiagHighLaserTempWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,24),_SfpDiagHighLaserTempWrnThreshold_Type())
sfpDiagHighLaserTempWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighLaserTempWrnThreshold.setStatus(_A)
class _SfpDiagLowLaserTempWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowLaserTempWrnThreshold_Type.__name__=_D
_SfpDiagLowLaserTempWrnThreshold_Object=MibTableColumn
sfpDiagLowLaserTempWrnThreshold=_SfpDiagLowLaserTempWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,25),_SfpDiagLowLaserTempWrnThreshold_Type())
sfpDiagLowLaserTempWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowLaserTempWrnThreshold.setStatus(_A)
class _SfpDiagHighWaveLenAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighWaveLenAlmThreshold_Type.__name__=_D
_SfpDiagHighWaveLenAlmThreshold_Object=MibTableColumn
sfpDiagHighWaveLenAlmThreshold=_SfpDiagHighWaveLenAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,26),_SfpDiagHighWaveLenAlmThreshold_Type())
sfpDiagHighWaveLenAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighWaveLenAlmThreshold.setStatus(_A)
class _SfpDiagLowWaveLenAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowWaveLenAlmThreshold_Type.__name__=_D
_SfpDiagLowWaveLenAlmThreshold_Object=MibTableColumn
sfpDiagLowWaveLenAlmThreshold=_SfpDiagLowWaveLenAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,27),_SfpDiagLowWaveLenAlmThreshold_Type())
sfpDiagLowWaveLenAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowWaveLenAlmThreshold.setStatus(_A)
class _SfpDiagHighWaveLenWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighWaveLenWrnThreshold_Type.__name__=_D
_SfpDiagHighWaveLenWrnThreshold_Object=MibTableColumn
sfpDiagHighWaveLenWrnThreshold=_SfpDiagHighWaveLenWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,28),_SfpDiagHighWaveLenWrnThreshold_Type())
sfpDiagHighWaveLenWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighWaveLenWrnThreshold.setStatus(_A)
class _SfpDiagLowWaveLenWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowWaveLenWrnThreshold_Type.__name__=_D
_SfpDiagLowWaveLenWrnThreshold_Object=MibTableColumn
sfpDiagLowWaveLenWrnThreshold=_SfpDiagLowWaveLenWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,29),_SfpDiagLowWaveLenWrnThreshold_Type())
sfpDiagLowWaveLenWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowWaveLenWrnThreshold.setStatus(_A)
class _SfpDiagHighTecCurrAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighTecCurrAlmThreshold_Type.__name__=_D
_SfpDiagHighTecCurrAlmThreshold_Object=MibTableColumn
sfpDiagHighTecCurrAlmThreshold=_SfpDiagHighTecCurrAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,30),_SfpDiagHighTecCurrAlmThreshold_Type())
sfpDiagHighTecCurrAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighTecCurrAlmThreshold.setStatus(_A)
class _SfpDiagLowTecCurrAlmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowTecCurrAlmThreshold_Type.__name__=_D
_SfpDiagLowTecCurrAlmThreshold_Object=MibTableColumn
sfpDiagLowTecCurrAlmThreshold=_SfpDiagLowTecCurrAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,31),_SfpDiagLowTecCurrAlmThreshold_Type())
sfpDiagLowTecCurrAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowTecCurrAlmThreshold.setStatus(_A)
class _SfpDiagHighTecCurrWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagHighTecCurrWrnThreshold_Type.__name__=_D
_SfpDiagHighTecCurrWrnThreshold_Object=MibTableColumn
sfpDiagHighTecCurrWrnThreshold=_SfpDiagHighTecCurrWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,32),_SfpDiagHighTecCurrWrnThreshold_Type())
sfpDiagHighTecCurrWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagHighTecCurrWrnThreshold.setStatus(_A)
class _SfpDiagLowTecCurrWrnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagLowTecCurrWrnThreshold_Type.__name__=_D
_SfpDiagLowTecCurrWrnThreshold_Object=MibTableColumn
sfpDiagLowTecCurrWrnThreshold=_SfpDiagLowTecCurrWrnThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,33),_SfpDiagLowTecCurrWrnThreshold_Type())
sfpDiagLowTecCurrWrnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagLowTecCurrWrnThreshold.setStatus(_A)
class _SfpDiagModuleTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagModuleTemperature_Type.__name__=_D
_SfpDiagModuleTemperature_Object=MibTableColumn
sfpDiagModuleTemperature=_SfpDiagModuleTemperature_Object((1,3,6,1,4,1,4515,1,10,2,1,1,34),_SfpDiagModuleTemperature_Type())
sfpDiagModuleTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagModuleTemperature.setStatus(_A)
class _SfpDiagSupplyVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagSupplyVoltage_Type.__name__=_D
_SfpDiagSupplyVoltage_Object=MibTableColumn
sfpDiagSupplyVoltage=_SfpDiagSupplyVoltage_Object((1,3,6,1,4,1,4515,1,10,2,1,1,35),_SfpDiagSupplyVoltage_Type())
sfpDiagSupplyVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagSupplyVoltage.setStatus(_A)
class _SfpDiagTxBias_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagTxBias_Type.__name__=_D
_SfpDiagTxBias_Object=MibTableColumn
sfpDiagTxBias=_SfpDiagTxBias_Object((1,3,6,1,4,1,4515,1,10,2,1,1,36),_SfpDiagTxBias_Type())
sfpDiagTxBias.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagTxBias.setStatus(_A)
class _SfpDiagTxOutputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagTxOutputPower_Type.__name__=_D
_SfpDiagTxOutputPower_Object=MibTableColumn
sfpDiagTxOutputPower=_SfpDiagTxOutputPower_Object((1,3,6,1,4,1,4515,1,10,2,1,1,37),_SfpDiagTxOutputPower_Type())
sfpDiagTxOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagTxOutputPower.setStatus(_A)
class _SfpDiagRxInputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagRxInputPower_Type.__name__=_D
_SfpDiagRxInputPower_Object=MibTableColumn
sfpDiagRxInputPower=_SfpDiagRxInputPower_Object((1,3,6,1,4,1,4515,1,10,2,1,1,38),_SfpDiagRxInputPower_Type())
sfpDiagRxInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagRxInputPower.setStatus(_A)
class _SfpDiagRxLaserTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagRxLaserTemperature_Type.__name__=_D
_SfpDiagRxLaserTemperature_Object=MibTableColumn
sfpDiagRxLaserTemperature=_SfpDiagRxLaserTemperature_Object((1,3,6,1,4,1,4515,1,10,2,1,1,39),_SfpDiagRxLaserTemperature_Type())
sfpDiagRxLaserTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagRxLaserTemperature.setStatus(_A)
class _SfpDiagRxMeasuredWavelength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagRxMeasuredWavelength_Type.__name__=_D
_SfpDiagRxMeasuredWavelength_Object=MibTableColumn
sfpDiagRxMeasuredWavelength=_SfpDiagRxMeasuredWavelength_Object((1,3,6,1,4,1,4515,1,10,2,1,1,40),_SfpDiagRxMeasuredWavelength_Type())
sfpDiagRxMeasuredWavelength.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagRxMeasuredWavelength.setStatus(_A)
class _SfpDiagRxTecCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagRxTecCurrent_Type.__name__=_D
_SfpDiagRxTecCurrent_Object=MibTableColumn
sfpDiagRxTecCurrent=_SfpDiagRxTecCurrent_Object((1,3,6,1,4,1,4515,1,10,2,1,1,41),_SfpDiagRxTecCurrent_Type())
sfpDiagRxTecCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagRxTecCurrent.setStatus(_A)
_SfpDiagAlarms_Type=Integer32
_SfpDiagAlarms_Object=MibTableColumn
sfpDiagAlarms=_SfpDiagAlarms_Object((1,3,6,1,4,1,4515,1,10,2,1,1,42),_SfpDiagAlarms_Type())
sfpDiagAlarms.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagAlarms.setStatus(_A)
_SfpDiagAlarmsMask_Type=Integer32
_SfpDiagAlarmsMask_Object=MibTableColumn
sfpDiagAlarmsMask=_SfpDiagAlarmsMask_Object((1,3,6,1,4,1,4515,1,10,2,1,1,43),_SfpDiagAlarmsMask_Type())
sfpDiagAlarmsMask.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagAlarmsMask.setStatus(_A)
_SfpDiagWarnings_Type=Integer32
_SfpDiagWarnings_Object=MibTableColumn
sfpDiagWarnings=_SfpDiagWarnings_Object((1,3,6,1,4,1,4515,1,10,2,1,1,44),_SfpDiagWarnings_Type())
sfpDiagWarnings.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagWarnings.setStatus(_A)
_SfpDiagWarningsMask_Type=Integer32
_SfpDiagWarningsMask_Object=MibTableColumn
sfpDiagWarningsMask=_SfpDiagWarningsMask_Object((1,3,6,1,4,1,4515,1,10,2,1,1,45),_SfpDiagWarningsMask_Type())
sfpDiagWarningsMask.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagWarningsMask.setStatus(_A)
_SfpDiagConfLowRxPowerAlmThreshold_Type=Integer32
_SfpDiagConfLowRxPowerAlmThreshold_Object=MibTableColumn
sfpDiagConfLowRxPowerAlmThreshold=_SfpDiagConfLowRxPowerAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,46),_SfpDiagConfLowRxPowerAlmThreshold_Type())
sfpDiagConfLowRxPowerAlmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpDiagConfLowRxPowerAlmThreshold.setStatus(_A)
_SfpDiagRxInputPowerFloat_Type=Float32TC
_SfpDiagRxInputPowerFloat_Object=MibTableColumn
sfpDiagRxInputPowerFloat=_SfpDiagRxInputPowerFloat_Object((1,3,6,1,4,1,4515,1,10,2,1,1,47),_SfpDiagRxInputPowerFloat_Type())
sfpDiagRxInputPowerFloat.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagRxInputPowerFloat.setStatus(_A)
class _SfpDiagChannelRxInputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpDiagChannelRxInputPower_Type.__name__=_D
_SfpDiagChannelRxInputPower_Object=MibTableColumn
sfpDiagChannelRxInputPower=_SfpDiagChannelRxInputPower_Object((1,3,6,1,4,1,4515,1,10,2,1,1,48),_SfpDiagChannelRxInputPower_Type())
sfpDiagChannelRxInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagChannelRxInputPower.setStatus(_A)
_SfpDiagCxpTxTemp_Type=Integer32
_SfpDiagCxpTxTemp_Object=MibTableColumn
sfpDiagCxpTxTemp=_SfpDiagCxpTxTemp_Object((1,3,6,1,4,1,4515,1,10,2,1,1,50),_SfpDiagCxpTxTemp_Type())
sfpDiagCxpTxTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagCxpTxTemp.setStatus(_A)
_SfpDiagCxpHighTxTempAlmThreshold_Type=Integer32
_SfpDiagCxpHighTxTempAlmThreshold_Object=MibTableColumn
sfpDiagCxpHighTxTempAlmThreshold=_SfpDiagCxpHighTxTempAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,51),_SfpDiagCxpHighTxTempAlmThreshold_Type())
sfpDiagCxpHighTxTempAlmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagCxpHighTxTempAlmThreshold.setStatus(_A)
_SfpDiagCxpLowTxTempAlmThreshold_Type=Integer32
_SfpDiagCxpLowTxTempAlmThreshold_Object=MibTableColumn
sfpDiagCxpLowTxTempAlmThreshold=_SfpDiagCxpLowTxTempAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,52),_SfpDiagCxpLowTxTempAlmThreshold_Type())
sfpDiagCxpLowTxTempAlmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagCxpLowTxTempAlmThreshold.setStatus(_A)
_SfpDiagCxpRxTemp_Type=Integer32
_SfpDiagCxpRxTemp_Object=MibTableColumn
sfpDiagCxpRxTemp=_SfpDiagCxpRxTemp_Object((1,3,6,1,4,1,4515,1,10,2,1,1,53),_SfpDiagCxpRxTemp_Type())
sfpDiagCxpRxTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagCxpRxTemp.setStatus(_A)
_SfpDiagCxpHighRxTempAlmThreshold_Type=Integer32
_SfpDiagCxpHighRxTempAlmThreshold_Object=MibTableColumn
sfpDiagCxpHighRxTempAlmThreshold=_SfpDiagCxpHighRxTempAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,54),_SfpDiagCxpHighRxTempAlmThreshold_Type())
sfpDiagCxpHighRxTempAlmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagCxpHighRxTempAlmThreshold.setStatus(_A)
_SfpDiagCxpLowRxTempAlmThreshold_Type=Integer32
_SfpDiagCxpLowRxTempAlmThreshold_Object=MibTableColumn
sfpDiagCxpLowRxTempAlmThreshold=_SfpDiagCxpLowRxTempAlmThreshold_Object((1,3,6,1,4,1,4515,1,10,2,1,1,55),_SfpDiagCxpLowRxTempAlmThreshold_Type())
sfpDiagCxpLowRxTempAlmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagCxpLowRxTempAlmThreshold.setStatus(_A)
_SfpDiagOtdrFiberCutRange_Type=Integer32
_SfpDiagOtdrFiberCutRange_Object=MibTableColumn
sfpDiagOtdrFiberCutRange=_SfpDiagOtdrFiberCutRange_Object((1,3,6,1,4,1,4515,1,10,2,1,1,56),_SfpDiagOtdrFiberCutRange_Type())
sfpDiagOtdrFiberCutRange.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagOtdrFiberCutRange.setStatus(_A)
_SfpDiagModuleTemperatureCelsius_Type=Integer32
_SfpDiagModuleTemperatureCelsius_Object=MibTableColumn
sfpDiagModuleTemperatureCelsius=_SfpDiagModuleTemperatureCelsius_Object((1,3,6,1,4,1,4515,1,10,2,1,1,57),_SfpDiagModuleTemperatureCelsius_Type())
sfpDiagModuleTemperatureCelsius.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpDiagModuleTemperatureCelsius.setStatus(_A)
_SfpTraps_ObjectIdentity=ObjectIdentity
sfpTraps=_SfpTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,10,3))
_SfpTune_ObjectIdentity=ObjectIdentity
sfpTune=_SfpTune_ObjectIdentity((1,3,6,1,4,1,4515,1,10,4))
sfpConfigChangeTrap=NotificationType((1,3,6,1,4,1,4515,1,10,3,1))
sfpConfigChangeTrap.setObjects((_F,_G))
if mibBuilder.loadTexts:sfpConfigChangeTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'slSfp':slSfp,'sfpConf':sfpConf,'sfpConfigTable':sfpConfigTable,'sfpConfigEntry':sfpConfigEntry,_G:sfpConfigInterface,'sfpConfigXcvrId':sfpConfigXcvrId,'sfpConfig1310ExtXcvrId':sfpConfig1310ExtXcvrId,'sfpConfigWdmExtXcvrId':sfpConfigWdmExtXcvrId,'sfpConfigConnectorCode':sfpConfigConnectorCode,'sfpConfigInfibandCompliance':sfpConfigInfibandCompliance,'sfpConfigEsconCompliance':sfpConfigEsconCompliance,'sfpConfigSonetCompliance':sfpConfigSonetCompliance,'sfpConfigGbeCompliance':sfpConfigGbeCompliance,'sfpConfigFcCompliance':sfpConfigFcCompliance,'sfpConfigEncodingCode':sfpConfigEncodingCode,'sfpConfigNominalBitRate':sfpConfigNominalBitRate,'sfpConfigLength9mKm':sfpConfigLength9mKm,'sfpConfigLength9m100m':sfpConfigLength9m100m,'sfpConfigLength50m10m':sfpConfigLength50m10m,'sfpConfigLength62m10m':sfpConfigLength62m10m,'sfpConfigLengthCopper1m':sfpConfigLengthCopper1m,'sfpConfigMaxTemp':sfpConfigMaxTemp,'sfpConfigMinTemp':sfpConfigMinTemp,'sfpConfigMaxSupplyCurrent':sfpConfigMaxSupplyCurrent,'sfpConfigChannelSpacing':sfpConfigChannelSpacing,'sfpConfigVendorName':sfpConfigVendorName,'sfpConfigOptionalWdm':sfpConfigOptionalWdm,'sfpConfigVendorOUI':sfpConfigVendorOUI,'sfpConfigVendorPN':sfpConfigVendorPN,'sfpConfigVendorRev':sfpConfigVendorRev,'sfpConfigWaveLength':sfpConfigWaveLength,'sfpConfigExtendedOptions':sfpConfigExtendedOptions,'sfpConfigMaxBitRate':sfpConfigMaxBitRate,'sfpConfigMinBitRate':sfpConfigMinBitRate,'sfpConfigVendorSN':sfpConfigVendorSN,'sfpConfigDateCode':sfpConfigDateCode,'sfpConfigDiagnosticMonitoring':sfpConfigDiagnosticMonitoring,'sfpConfigEnhanceOptions':sfpConfigEnhanceOptions,'sfpConfig8472Compliance':sfpConfig8472Compliance,'sfpConfigTunableWaveLength':sfpConfigTunableWaveLength,'sfpConfigVoaControl':sfpConfigVoaControl,'sfpConfigVdtControl':sfpConfigVdtControl,'sfpConfigPilotToneModulation':sfpConfigPilotToneModulation,'sfpConfigCleiCode':sfpConfigCleiCode,'sfpConfigXfpExtXcvrId':sfpConfigXfpExtXcvrId,'sfpConfigXfpEncodingCode':sfpConfigXfpEncodingCode,'sfpConfigXfpMinBitRate':sfpConfigXfpMinBitRate,'sfpConfigXfpMaxBitRate':sfpConfigXfpMaxBitRate,'sfpConfig10GSonetCompliance':sfpConfig10GSonetCompliance,'sfpConfig10GbeCompliance':sfpConfig10GbeCompliance,'sfpConfig10GFcCompliance':sfpConfig10GFcCompliance,'sfpConfigXfpDeviceTech':sfpConfigXfpDeviceTech,'sfpConfigXfpTuningSupported':sfpConfigXfpTuningSupported,'sfpConfigXfpDesiredChannel':sfpConfigXfpDesiredChannel,'sfpConfigXfpDesiredWl':sfpConfigXfpDesiredWl,'sfpConfigXfpWlError':sfpConfigXfpWlError,'sfpConfigXfpDesiredFreq':sfpConfigXfpDesiredFreq,'sfpConfigXfpFreqError':sfpConfigXfpFreqError,'sfpConfigXfpDitherSupported':sfpConfigXfpDitherSupported,'sfpConfigXfpDitherAdmin':sfpConfigXfpDitherAdmin,'sfpConfigXfpCapFreqFirstThz':sfpConfigXfpCapFreqFirstThz,'sfpConfigXfpCapFreqFirst10Ghz':sfpConfigXfpCapFreqFirst10Ghz,'sfpConfigXfpCapFreqLastThz':sfpConfigXfpCapFreqLastThz,'sfpConfigXfpCapFreqLast10Ghz':sfpConfigXfpCapFreqLast10Ghz,'sfpConfigXfpCapMaxSpacing10Ghz':sfpConfigXfpCapMaxSpacing10Ghz,'sfpConfigXfpCalibrationSupported':sfpConfigXfpCalibrationSupported,'sfpConfigXfpCalibrationEnabled':sfpConfigXfpCalibrationEnabled,'sfpConfigCfpExtId':sfpConfigCfpExtId,'sfpConfigCfpConnectorType':sfpConfigCfpConnectorType,'sfpConfigCfpEthernetCode':sfpConfigCfpEthernetCode,'sfpConfigCfpFcCode':sfpConfigCfpFcCode,'sfpConfigCfpCopperCode':sfpConfigCfpCopperCode,'sfpConfigCfpSonetCode':sfpConfigCfpSonetCode,'sfpConfigCfpOtnCode':sfpConfigCfpOtnCode,'sfpConfigCfpSupportedRates':sfpConfigCfpSupportedRates,'sfpConfigCfpSupportedLanes':sfpConfigCfpSupportedLanes,'sfpConfigCfpMediaProperties':sfpConfigCfpMediaProperties,'sfpConfigCfpMaxNetworkLaneRate':sfpConfigCfpMaxNetworkLaneRate,'sfpConfigCfpMaxHostLaneRate':sfpConfigCfpMaxHostLaneRate,'sfpConfigCfpMaxSmFiberLength':sfpConfigCfpMaxSmFiberLength,'sfpConfigCfpMaxMmFiberLength':sfpConfigCfpMaxMmFiberLength,'sfpConfigCfpMaxCopperCableLength':sfpConfigCfpMaxCopperCableLength,'sfpConfigCfpMinWavelenPerActive':sfpConfigCfpMinWavelenPerActive,'sfpConfigCfpMaxWavelenPerActive':sfpConfigCfpMaxWavelenPerActive,'sfpConfigCfpMaxLenOpticalWidth':sfpConfigCfpMaxLenOpticalWidth,'sfpConfigCfpSpacing':sfpConfigCfpSpacing,'sfpConfigQsfppEthernetCode':sfpConfigQsfppEthernetCode,'sfpConfigQsfppSonetCode':sfpConfigQsfppSonetCode,'sfpConfigCxpExtId':sfpConfigCxpExtId,'sfpConfigCxpConnectorType':sfpConfigCxpConnectorType,'sfpConfigCxpMaxSupportedRate':sfpConfigCxpMaxSupportedRate,'sfpConfigCxpNominalWavelength':sfpConfigCxpNominalWavelength,'sfpConfigCxpDeviceTech':sfpConfigCxpDeviceTech,'sfpConfigCohRxDesiredChannel':sfpConfigCohRxDesiredChannel,'sfpConfigCohRxDesiredWl':sfpConfigCohRxDesiredWl,'sfpConfigCohRxDesiredFreq':sfpConfigCohRxDesiredFreq,'sfpConfigCohCurrentCD':sfpConfigCohCurrentCD,'sfpConfigCohCurrentOSNR':sfpConfigCohCurrentOSNR,'sfpConfigCohAverageOSNR':sfpConfigCohAverageOSNR,'sfpConfigCohMaxCD':sfpConfigCohMaxCD,'sfpConfigNyquist':sfpConfigNyquist,'sfpConfigModulationFormat':sfpConfigModulationFormat,'sfpDiag':sfpDiag,'sfpDiagTable':sfpDiagTable,'sfpDiagEntry':sfpDiagEntry,_I:sfpDiagInterface,'sfpDiagHighTempAlmThreshold':sfpDiagHighTempAlmThreshold,'sfpDiagLowTempAlmThreshold':sfpDiagLowTempAlmThreshold,'sfpDiagHighTempWrnThreshold':sfpDiagHighTempWrnThreshold,'sfpDiagLowTempWrnThreshold':sfpDiagLowTempWrnThreshold,'sfpDiagHighVoltAlmThreshold':sfpDiagHighVoltAlmThreshold,'sfpDiagLowVoltAlmThreshold':sfpDiagLowVoltAlmThreshold,'sfpDiagHighVoltWrnThreshold':sfpDiagHighVoltWrnThreshold,'sfpDiagLowVoltWrnThreshold':sfpDiagLowVoltWrnThreshold,'sfpDiagHighTxBiasAlmThreshold':sfpDiagHighTxBiasAlmThreshold,'sfpDiagLowTxBiasAlmThreshold':sfpDiagLowTxBiasAlmThreshold,'sfpDiagHighTxBiasWrnThreshold':sfpDiagHighTxBiasWrnThreshold,'sfpDiagLowTxBiasWrnThreshold':sfpDiagLowTxBiasWrnThreshold,'sfpDiagHighTxPowerAlmThreshold':sfpDiagHighTxPowerAlmThreshold,'sfpDiagLowTxPowerAlmThreshold':sfpDiagLowTxPowerAlmThreshold,'sfpDiagHighTxPowerWrnThreshold':sfpDiagHighTxPowerWrnThreshold,'sfpDiagLowTxPowerWrnThreshold':sfpDiagLowTxPowerWrnThreshold,'sfpDiagHighRxPowerAlmThreshold':sfpDiagHighRxPowerAlmThreshold,'sfpDiagLowRxPowerAlmThreshold':sfpDiagLowRxPowerAlmThreshold,'sfpDiagHighRxPowerWrnThreshold':sfpDiagHighRxPowerWrnThreshold,'sfpDiagLowRxPowerWrnThreshold':sfpDiagLowRxPowerWrnThreshold,'sfpDiagHighLaserTempAlmThreshold':sfpDiagHighLaserTempAlmThreshold,'sfpDiagLowLaserTempAlmThreshold':sfpDiagLowLaserTempAlmThreshold,'sfpDiagHighLaserTempWrnThreshold':sfpDiagHighLaserTempWrnThreshold,'sfpDiagLowLaserTempWrnThreshold':sfpDiagLowLaserTempWrnThreshold,'sfpDiagHighWaveLenAlmThreshold':sfpDiagHighWaveLenAlmThreshold,'sfpDiagLowWaveLenAlmThreshold':sfpDiagLowWaveLenAlmThreshold,'sfpDiagHighWaveLenWrnThreshold':sfpDiagHighWaveLenWrnThreshold,'sfpDiagLowWaveLenWrnThreshold':sfpDiagLowWaveLenWrnThreshold,'sfpDiagHighTecCurrAlmThreshold':sfpDiagHighTecCurrAlmThreshold,'sfpDiagLowTecCurrAlmThreshold':sfpDiagLowTecCurrAlmThreshold,'sfpDiagHighTecCurrWrnThreshold':sfpDiagHighTecCurrWrnThreshold,'sfpDiagLowTecCurrWrnThreshold':sfpDiagLowTecCurrWrnThreshold,'sfpDiagModuleTemperature':sfpDiagModuleTemperature,'sfpDiagSupplyVoltage':sfpDiagSupplyVoltage,'sfpDiagTxBias':sfpDiagTxBias,'sfpDiagTxOutputPower':sfpDiagTxOutputPower,'sfpDiagRxInputPower':sfpDiagRxInputPower,'sfpDiagRxLaserTemperature':sfpDiagRxLaserTemperature,'sfpDiagRxMeasuredWavelength':sfpDiagRxMeasuredWavelength,'sfpDiagRxTecCurrent':sfpDiagRxTecCurrent,'sfpDiagAlarms':sfpDiagAlarms,'sfpDiagAlarmsMask':sfpDiagAlarmsMask,'sfpDiagWarnings':sfpDiagWarnings,'sfpDiagWarningsMask':sfpDiagWarningsMask,'sfpDiagConfLowRxPowerAlmThreshold':sfpDiagConfLowRxPowerAlmThreshold,'sfpDiagRxInputPowerFloat':sfpDiagRxInputPowerFloat,'sfpDiagChannelRxInputPower':sfpDiagChannelRxInputPower,'sfpDiagCxpTxTemp':sfpDiagCxpTxTemp,'sfpDiagCxpHighTxTempAlmThreshold':sfpDiagCxpHighTxTempAlmThreshold,'sfpDiagCxpLowTxTempAlmThreshold':sfpDiagCxpLowTxTempAlmThreshold,'sfpDiagCxpRxTemp':sfpDiagCxpRxTemp,'sfpDiagCxpHighRxTempAlmThreshold':sfpDiagCxpHighRxTempAlmThreshold,'sfpDiagCxpLowRxTempAlmThreshold':sfpDiagCxpLowRxTempAlmThreshold,'sfpDiagOtdrFiberCutRange':sfpDiagOtdrFiberCutRange,'sfpDiagModuleTemperatureCelsius':sfpDiagModuleTemperatureCelsius,'sfpTraps':sfpTraps,'sfpConfigChangeTrap':sfpConfigChangeTrap,'sfpTune':sfpTune})
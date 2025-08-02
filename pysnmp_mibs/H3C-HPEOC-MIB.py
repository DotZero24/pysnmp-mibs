_Q='h3cHPEOCCnuAccessIndex'
_P='h3cHPEOCTemplateUniIndex'
_O='gateway'
_N='switch'
_M='not-accessible'
_L='h3cHPEOCBitPerSymbolIndex'
_K='DisplayString'
_J='h3cHPEOCTemplateIndex'
_I='TruthValue'
_H='read-create'
_G='H3C-HPEOC-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'MacAddress','PhysAddress','RowStatus','TextualConvention',_I)
h3cHPEOC=ModuleIdentity((1,3,6,1,4,1,2011,10,2,84))
_H3cHPEOCSystem_ObjectIdentity=ObjectIdentity
h3cHPEOCSystem=_H3cHPEOCSystem_ObjectIdentity((1,3,6,1,4,1,2011,10,2,84,1))
class _H3cHPEOCCltVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ieee8021q',1),('portbased',2)))
_H3cHPEOCCltVlanType_Type.__name__=_C
_H3cHPEOCCltVlanType_Object=MibScalar
h3cHPEOCCltVlanType=_H3cHPEOCCltVlanType_Object((1,3,6,1,4,1,2011,10,2,84,1,1),_H3cHPEOCCltVlanType_Type())
h3cHPEOCCltVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCCltVlanType.setStatus(_A)
_H3cHPEOCCltVlanManTable_Object=MibTable
h3cHPEOCCltVlanManTable=_H3cHPEOCCltVlanManTable_Object((1,3,6,1,4,1,2011,10,2,84,1,2))
if mibBuilder.loadTexts:h3cHPEOCCltVlanManTable.setStatus(_A)
_H3cHPEOCCltVlanManEntry_Object=MibTableRow
h3cHPEOCCltVlanManEntry=_H3cHPEOCCltVlanManEntry_Object((1,3,6,1,4,1,2011,10,2,84,1,2,1))
h3cHPEOCCltVlanManEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:h3cHPEOCCltVlanManEntry.setStatus(_A)
class _H3cHPEOCCltEthPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('debug',2)))
_H3cHPEOCCltEthPortType_Type.__name__=_C
_H3cHPEOCCltEthPortType_Object=MibTableColumn
h3cHPEOCCltEthPortType=_H3cHPEOCCltEthPortType_Object((1,3,6,1,4,1,2011,10,2,84,1,2,1,1),_H3cHPEOCCltEthPortType_Type())
h3cHPEOCCltEthPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCCltEthPortType.setStatus(_A)
_H3cHPEOCCltSysManTable_Object=MibTable
h3cHPEOCCltSysManTable=_H3cHPEOCCltSysManTable_Object((1,3,6,1,4,1,2011,10,2,84,1,3))
if mibBuilder.loadTexts:h3cHPEOCCltSysManTable.setStatus(_A)
_H3cHPEOCCltSysManEntry_Object=MibTableRow
h3cHPEOCCltSysManEntry=_H3cHPEOCCltSysManEntry_Object((1,3,6,1,4,1,2011,10,2,84,1,3,1))
h3cHPEOCCltSysManEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:h3cHPEOCCltSysManEntry.setStatus(_A)
class _H3cHPEOCCltDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,126))
_H3cHPEOCCltDescr_Type.__name__=_K
_H3cHPEOCCltDescr_Object=MibTableColumn
h3cHPEOCCltDescr=_H3cHPEOCCltDescr_Object((1,3,6,1,4,1,2011,10,2,84,1,3,1,1),_H3cHPEOCCltDescr_Type())
h3cHPEOCCltDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCCltDescr.setStatus(_A)
_H3cHPEOCCltFwVersion_Type=DisplayString
_H3cHPEOCCltFwVersion_Object=MibTableColumn
h3cHPEOCCltFwVersion=_H3cHPEOCCltFwVersion_Object((1,3,6,1,4,1,2011,10,2,84,1,3,1,2),_H3cHPEOCCltFwVersion_Type())
h3cHPEOCCltFwVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCCltFwVersion.setStatus(_A)
class _H3cHPEOCCltLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('physicaldown',1),('linkdown',2),('linkup',3),('loopback',4)))
_H3cHPEOCCltLinkState_Type.__name__=_C
_H3cHPEOCCltLinkState_Object=MibTableColumn
h3cHPEOCCltLinkState=_H3cHPEOCCltLinkState_Object((1,3,6,1,4,1,2011,10,2,84,1,3,1,3),_H3cHPEOCCltLinkState_Type())
h3cHPEOCCltLinkState.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCCltLinkState.setStatus(_A)
_H3cHPEOCCnuSysManTable_Object=MibTable
h3cHPEOCCnuSysManTable=_H3cHPEOCCnuSysManTable_Object((1,3,6,1,4,1,2011,10,2,84,1,4))
if mibBuilder.loadTexts:h3cHPEOCCnuSysManTable.setStatus(_A)
_H3cHPEOCCnuSysManEntry_Object=MibTableRow
h3cHPEOCCnuSysManEntry=_H3cHPEOCCnuSysManEntry_Object((1,3,6,1,4,1,2011,10,2,84,1,4,1))
h3cHPEOCCnuSysManEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:h3cHPEOCCnuSysManEntry.setStatus(_A)
_H3cHPEOCCnuBcastControl_Type=TruthValue
_H3cHPEOCCnuBcastControl_Object=MibTableColumn
h3cHPEOCCnuBcastControl=_H3cHPEOCCnuBcastControl_Object((1,3,6,1,4,1,2011,10,2,84,1,4,1,1),_H3cHPEOCCnuBcastControl_Type())
h3cHPEOCCnuBcastControl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCCnuBcastControl.setStatus(_A)
_H3cHPEOCCnuAnonymStatus_Type=TruthValue
_H3cHPEOCCnuAnonymStatus_Object=MibTableColumn
h3cHPEOCCnuAnonymStatus=_H3cHPEOCCnuAnonymStatus_Object((1,3,6,1,4,1,2011,10,2,84,1,4,1,2),_H3cHPEOCCnuAnonymStatus_Type())
h3cHPEOCCnuAnonymStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCCnuAnonymStatus.setStatus(_A)
_H3cHPEOCCnuMacLimit_Type=Unsigned32
_H3cHPEOCCnuMacLimit_Object=MibTableColumn
h3cHPEOCCnuMacLimit=_H3cHPEOCCnuMacLimit_Object((1,3,6,1,4,1,2011,10,2,84,1,4,1,3),_H3cHPEOCCnuMacLimit_Type())
h3cHPEOCCnuMacLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCCnuMacLimit.setStatus(_A)
class _H3cHPEOCCltAutoUpgrade_Type(TruthValue):defaultValue=2
_H3cHPEOCCltAutoUpgrade_Type.__name__=_I
_H3cHPEOCCltAutoUpgrade_Object=MibScalar
h3cHPEOCCltAutoUpgrade=_H3cHPEOCCltAutoUpgrade_Object((1,3,6,1,4,1,2011,10,2,84,1,5),_H3cHPEOCCltAutoUpgrade_Type())
h3cHPEOCCltAutoUpgrade.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCCltAutoUpgrade.setStatus(_A)
_H3cHPEOCOnLineCnuNumber_Type=Integer32
_H3cHPEOCOnLineCnuNumber_Object=MibScalar
h3cHPEOCOnLineCnuNumber=_H3cHPEOCOnLineCnuNumber_Object((1,3,6,1,4,1,2011,10,2,84,1,6),_H3cHPEOCOnLineCnuNumber_Type())
h3cHPEOCOnLineCnuNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCOnLineCnuNumber.setStatus(_A)
_H3cHPEOCCpuMacAddress_Type=MacAddress
_H3cHPEOCCpuMacAddress_Object=MibScalar
h3cHPEOCCpuMacAddress=_H3cHPEOCCpuMacAddress_Object((1,3,6,1,4,1,2011,10,2,84,1,7),_H3cHPEOCCpuMacAddress_Type())
h3cHPEOCCpuMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCCpuMacAddress.setStatus(_A)
_H3cHPEOCOffLineCnuNumber_Type=Integer32
_H3cHPEOCOffLineCnuNumber_Object=MibScalar
h3cHPEOCOffLineCnuNumber=_H3cHPEOCOffLineCnuNumber_Object((1,3,6,1,4,1,2011,10,2,84,1,8),_H3cHPEOCOffLineCnuNumber_Type())
h3cHPEOCOffLineCnuNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCOffLineCnuNumber.setStatus(_A)
_H3cHPEOCDownLoadCNUFWResult_Type=DisplayString
_H3cHPEOCDownLoadCNUFWResult_Object=MibScalar
h3cHPEOCDownLoadCNUFWResult=_H3cHPEOCDownLoadCNUFWResult_Object((1,3,6,1,4,1,2011,10,2,84,1,9),_H3cHPEOCDownLoadCNUFWResult_Type())
h3cHPEOCDownLoadCNUFWResult.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cHPEOCDownLoadCNUFWResult.setStatus(_A)
class _H3cHPEOCCltAutoUpgradeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('flash',1),('ftp',2),('tftp',3)))
_H3cHPEOCCltAutoUpgradeType_Type.__name__=_C
_H3cHPEOCCltAutoUpgradeType_Object=MibScalar
h3cHPEOCCltAutoUpgradeType=_H3cHPEOCCltAutoUpgradeType_Object((1,3,6,1,4,1,2011,10,2,84,1,10),_H3cHPEOCCltAutoUpgradeType_Type())
h3cHPEOCCltAutoUpgradeType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCCltAutoUpgradeType.setStatus(_A)
_H3cHPEOCAutoUpObjects_ObjectIdentity=ObjectIdentity
h3cHPEOCAutoUpObjects=_H3cHPEOCAutoUpObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,84,1,11))
_H3cHPEOCServerAddress_Type=IpAddress
_H3cHPEOCServerAddress_Object=MibScalar
h3cHPEOCServerAddress=_H3cHPEOCServerAddress_Object((1,3,6,1,4,1,2011,10,2,84,1,11,1),_H3cHPEOCServerAddress_Type())
h3cHPEOCServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCServerAddress.setStatus(_A)
_H3cHPEOCServerUser_Type=DisplayString
_H3cHPEOCServerUser_Object=MibScalar
h3cHPEOCServerUser=_H3cHPEOCServerUser_Object((1,3,6,1,4,1,2011,10,2,84,1,11,2),_H3cHPEOCServerUser_Type())
h3cHPEOCServerUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCServerUser.setStatus(_A)
_H3cHPEOCServerPassword_Type=DisplayString
_H3cHPEOCServerPassword_Object=MibScalar
h3cHPEOCServerPassword=_H3cHPEOCServerPassword_Object((1,3,6,1,4,1,2011,10,2,84,1,11,3),_H3cHPEOCServerPassword_Type())
h3cHPEOCServerPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCServerPassword.setStatus(_A)
class _H3cHPEOCCltLoopbackDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_H3cHPEOCCltLoopbackDetect_Type.__name__=_C
_H3cHPEOCCltLoopbackDetect_Object=MibScalar
h3cHPEOCCltLoopbackDetect=_H3cHPEOCCltLoopbackDetect_Object((1,3,6,1,4,1,2011,10,2,84,1,12),_H3cHPEOCCltLoopbackDetect_Type())
h3cHPEOCCltLoopbackDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCCltLoopbackDetect.setStatus(_A)
class _H3cHPEOCTemplateEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_H3cHPEOCTemplateEnable_Type.__name__=_C
_H3cHPEOCTemplateEnable_Object=MibScalar
h3cHPEOCTemplateEnable=_H3cHPEOCTemplateEnable_Object((1,3,6,1,4,1,2011,10,2,84,1,13),_H3cHPEOCTemplateEnable_Type())
h3cHPEOCTemplateEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateEnable.setStatus(_A)
_H3cHPEOCCableInfo_ObjectIdentity=ObjectIdentity
h3cHPEOCCableInfo=_H3cHPEOCCableInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,84,2))
_H3cHPEOCCableInfoTable_Object=MibTable
h3cHPEOCCableInfoTable=_H3cHPEOCCableInfoTable_Object((1,3,6,1,4,1,2011,10,2,84,2,1))
if mibBuilder.loadTexts:h3cHPEOCCableInfoTable.setStatus(_A)
_H3cHPEOCCableInfoEntry_Object=MibTableRow
h3cHPEOCCableInfoEntry=_H3cHPEOCCableInfoEntry_Object((1,3,6,1,4,1,2011,10,2,84,2,1,1))
h3cHPEOCCableInfoEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:h3cHPEOCCableInfoEntry.setStatus(_A)
_H3cHPEOCFECErrors_Type=Counter64
_H3cHPEOCFECErrors_Object=MibTableColumn
h3cHPEOCFECErrors=_H3cHPEOCFECErrors_Object((1,3,6,1,4,1,2011,10,2,84,2,1,1,1),_H3cHPEOCFECErrors_Type())
h3cHPEOCFECErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCFECErrors.setStatus(_A)
_H3cHPEOCAvgBitsPerCarrier_Type=Unsigned32
_H3cHPEOCAvgBitsPerCarrier_Object=MibTableColumn
h3cHPEOCAvgBitsPerCarrier=_H3cHPEOCAvgBitsPerCarrier_Object((1,3,6,1,4,1,2011,10,2,84,2,1,1,2),_H3cHPEOCAvgBitsPerCarrier_Type())
h3cHPEOCAvgBitsPerCarrier.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCAvgBitsPerCarrier.setStatus(_A)
_H3cHPEOCAvgSNRPerCarrier_Type=Integer32
_H3cHPEOCAvgSNRPerCarrier_Object=MibTableColumn
h3cHPEOCAvgSNRPerCarrier=_H3cHPEOCAvgSNRPerCarrier_Object((1,3,6,1,4,1,2011,10,2,84,2,1,1,3),_H3cHPEOCAvgSNRPerCarrier_Type())
h3cHPEOCAvgSNRPerCarrier.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCAvgSNRPerCarrier.setStatus(_A)
_H3cHPEOCAvgInPBCRCErrors_Type=Unsigned32
_H3cHPEOCAvgInPBCRCErrors_Object=MibTableColumn
h3cHPEOCAvgInPBCRCErrors=_H3cHPEOCAvgInPBCRCErrors_Object((1,3,6,1,4,1,2011,10,2,84,2,1,1,4),_H3cHPEOCAvgInPBCRCErrors_Type())
h3cHPEOCAvgInPBCRCErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCAvgInPBCRCErrors.setStatus(_A)
_H3cHPEOCInTotalPkts_Type=Counter64
_H3cHPEOCInTotalPkts_Object=MibTableColumn
h3cHPEOCInTotalPkts=_H3cHPEOCInTotalPkts_Object((1,3,6,1,4,1,2011,10,2,84,2,1,1,5),_H3cHPEOCInTotalPkts_Type())
h3cHPEOCInTotalPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCInTotalPkts.setStatus(_A)
_H3cHPEOCAvgOutPower_Type=Integer32
_H3cHPEOCAvgOutPower_Object=MibTableColumn
h3cHPEOCAvgOutPower=_H3cHPEOCAvgOutPower_Object((1,3,6,1,4,1,2011,10,2,84,2,1,1,6),_H3cHPEOCAvgOutPower_Type())
h3cHPEOCAvgOutPower.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCAvgOutPower.setStatus(_A)
_H3cHPEOCAvgOutPBCRCErrors_Type=Unsigned32
_H3cHPEOCAvgOutPBCRCErrors_Object=MibTableColumn
h3cHPEOCAvgOutPBCRCErrors=_H3cHPEOCAvgOutPBCRCErrors_Object((1,3,6,1,4,1,2011,10,2,84,2,1,1,7),_H3cHPEOCAvgOutPBCRCErrors_Type())
h3cHPEOCAvgOutPBCRCErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCAvgOutPBCRCErrors.setStatus(_A)
_H3cHPEOCOutTotalPkts_Type=Counter64
_H3cHPEOCOutTotalPkts_Object=MibTableColumn
h3cHPEOCOutTotalPkts=_H3cHPEOCOutTotalPkts_Object((1,3,6,1,4,1,2011,10,2,84,2,1,1,8),_H3cHPEOCOutTotalPkts_Type())
h3cHPEOCOutTotalPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCOutTotalPkts.setStatus(_A)
_H3cHPEOCBitPerSymbolTable_Object=MibTable
h3cHPEOCBitPerSymbolTable=_H3cHPEOCBitPerSymbolTable_Object((1,3,6,1,4,1,2011,10,2,84,2,2))
if mibBuilder.loadTexts:h3cHPEOCBitPerSymbolTable.setStatus(_A)
_H3cHPEOCBitPerSymbolEntry_Object=MibTableRow
h3cHPEOCBitPerSymbolEntry=_H3cHPEOCBitPerSymbolEntry_Object((1,3,6,1,4,1,2011,10,2,84,2,2,1))
h3cHPEOCBitPerSymbolEntry.setIndexNames((0,_E,_F),(0,_G,_L))
if mibBuilder.loadTexts:h3cHPEOCBitPerSymbolEntry.setStatus(_A)
_H3cHPEOCBitPerSymbolIndex_Type=Unsigned32
_H3cHPEOCBitPerSymbolIndex_Object=MibTableColumn
h3cHPEOCBitPerSymbolIndex=_H3cHPEOCBitPerSymbolIndex_Object((1,3,6,1,4,1,2011,10,2,84,2,2,1,1),_H3cHPEOCBitPerSymbolIndex_Type())
h3cHPEOCBitPerSymbolIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cHPEOCBitPerSymbolIndex.setStatus(_A)
_H3cHPEOCBitPerSymbol_Type=OctetString
_H3cHPEOCBitPerSymbol_Object=MibTableColumn
h3cHPEOCBitPerSymbol=_H3cHPEOCBitPerSymbol_Object((1,3,6,1,4,1,2011,10,2,84,2,2,1,2),_H3cHPEOCBitPerSymbol_Type())
h3cHPEOCBitPerSymbol.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHPEOCBitPerSymbol.setStatus(_A)
_H3cHPEOCTemplate_ObjectIdentity=ObjectIdentity
h3cHPEOCTemplate=_H3cHPEOCTemplate_ObjectIdentity((1,3,6,1,4,1,2011,10,2,84,3))
_H3cHPEOCTemplateGlobalTable_Object=MibTable
h3cHPEOCTemplateGlobalTable=_H3cHPEOCTemplateGlobalTable_Object((1,3,6,1,4,1,2011,10,2,84,3,1))
if mibBuilder.loadTexts:h3cHPEOCTemplateGlobalTable.setStatus(_A)
_H3cHPEOCTemplateGlobalEntry_Object=MibTableRow
h3cHPEOCTemplateGlobalEntry=_H3cHPEOCTemplateGlobalEntry_Object((1,3,6,1,4,1,2011,10,2,84,3,1,1))
h3cHPEOCTemplateGlobalEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:h3cHPEOCTemplateGlobalEntry.setStatus(_A)
_H3cHPEOCTemplateIndex_Type=Integer32
_H3cHPEOCTemplateIndex_Object=MibTableColumn
h3cHPEOCTemplateIndex=_H3cHPEOCTemplateIndex_Object((1,3,6,1,4,1,2011,10,2,84,3,1,1,1),_H3cHPEOCTemplateIndex_Type())
h3cHPEOCTemplateIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cHPEOCTemplateIndex.setStatus(_A)
class _H3cHPEOCTemplateType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cHPEOCTemplateType_Type.__name__=_C
_H3cHPEOCTemplateType_Object=MibTableColumn
h3cHPEOCTemplateType=_H3cHPEOCTemplateType_Object((1,3,6,1,4,1,2011,10,2,84,3,1,1,2),_H3cHPEOCTemplateType_Type())
h3cHPEOCTemplateType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cHPEOCTemplateType.setStatus(_A)
_H3cHPEOCTemplateName_Type=DisplayString
_H3cHPEOCTemplateName_Object=MibTableColumn
h3cHPEOCTemplateName=_H3cHPEOCTemplateName_Object((1,3,6,1,4,1,2011,10,2,84,3,1,1,3),_H3cHPEOCTemplateName_Type())
h3cHPEOCTemplateName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateName.setStatus(_A)
_H3cHPEOCTemplateDescr_Type=DisplayString
_H3cHPEOCTemplateDescr_Object=MibTableColumn
h3cHPEOCTemplateDescr=_H3cHPEOCTemplateDescr_Object((1,3,6,1,4,1,2011,10,2,84,3,1,1,4),_H3cHPEOCTemplateDescr_Type())
h3cHPEOCTemplateDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateDescr.setStatus(_A)
_H3cHPEOCTemplateCnuMaxDownBW_Type=Integer32
_H3cHPEOCTemplateCnuMaxDownBW_Object=MibTableColumn
h3cHPEOCTemplateCnuMaxDownBW=_H3cHPEOCTemplateCnuMaxDownBW_Object((1,3,6,1,4,1,2011,10,2,84,3,1,1,5),_H3cHPEOCTemplateCnuMaxDownBW_Type())
h3cHPEOCTemplateCnuMaxDownBW.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateCnuMaxDownBW.setStatus(_A)
_H3cHPEOCTemplateCnuMaxUpBW_Type=Integer32
_H3cHPEOCTemplateCnuMaxUpBW_Object=MibTableColumn
h3cHPEOCTemplateCnuMaxUpBW=_H3cHPEOCTemplateCnuMaxUpBW_Object((1,3,6,1,4,1,2011,10,2,84,3,1,1,6),_H3cHPEOCTemplateCnuMaxUpBW_Type())
h3cHPEOCTemplateCnuMaxUpBW.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateCnuMaxUpBW.setStatus(_A)
_H3cHPEOCTemplateCnuBcastControl_Type=TruthValue
_H3cHPEOCTemplateCnuBcastControl_Object=MibTableColumn
h3cHPEOCTemplateCnuBcastControl=_H3cHPEOCTemplateCnuBcastControl_Object((1,3,6,1,4,1,2011,10,2,84,3,1,1,7),_H3cHPEOCTemplateCnuBcastControl_Type())
h3cHPEOCTemplateCnuBcastControl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateCnuBcastControl.setStatus(_A)
_H3cHPEOCTemplateCnuMacLimit_Type=Unsigned32
_H3cHPEOCTemplateCnuMacLimit_Object=MibTableColumn
h3cHPEOCTemplateCnuMacLimit=_H3cHPEOCTemplateCnuMacLimit_Object((1,3,6,1,4,1,2011,10,2,84,3,1,1,8),_H3cHPEOCTemplateCnuMacLimit_Type())
h3cHPEOCTemplateCnuMacLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateCnuMacLimit.setStatus(_A)
_H3cHPEOCTemplateCb201VlanEn_Type=TruthValue
_H3cHPEOCTemplateCb201VlanEn_Object=MibTableColumn
h3cHPEOCTemplateCb201VlanEn=_H3cHPEOCTemplateCb201VlanEn_Object((1,3,6,1,4,1,2011,10,2,84,3,1,1,9),_H3cHPEOCTemplateCb201VlanEn_Type())
h3cHPEOCTemplateCb201VlanEn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateCb201VlanEn.setStatus(_A)
_H3cHPEOCTemplateRowStatus_Type=RowStatus
_H3cHPEOCTemplateRowStatus_Object=MibTableColumn
h3cHPEOCTemplateRowStatus=_H3cHPEOCTemplateRowStatus_Object((1,3,6,1,4,1,2011,10,2,84,3,1,1,10),_H3cHPEOCTemplateRowStatus_Type())
h3cHPEOCTemplateRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cHPEOCTemplateRowStatus.setStatus(_A)
_H3cHPEOCTemplateSwitchTable_Object=MibTable
h3cHPEOCTemplateSwitchTable=_H3cHPEOCTemplateSwitchTable_Object((1,3,6,1,4,1,2011,10,2,84,3,2))
if mibBuilder.loadTexts:h3cHPEOCTemplateSwitchTable.setStatus(_A)
_H3cHPEOCTemplateSwitchEntry_Object=MibTableRow
h3cHPEOCTemplateSwitchEntry=_H3cHPEOCTemplateSwitchEntry_Object((1,3,6,1,4,1,2011,10,2,84,3,2,1))
h3cHPEOCTemplateSwitchEntry.setIndexNames((0,_G,_J),(0,_G,_P))
if mibBuilder.loadTexts:h3cHPEOCTemplateSwitchEntry.setStatus(_A)
_H3cHPEOCTemplateUniIndex_Type=Integer32
_H3cHPEOCTemplateUniIndex_Object=MibTableColumn
h3cHPEOCTemplateUniIndex=_H3cHPEOCTemplateUniIndex_Object((1,3,6,1,4,1,2011,10,2,84,3,2,1,1),_H3cHPEOCTemplateUniIndex_Type())
h3cHPEOCTemplateUniIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cHPEOCTemplateUniIndex.setStatus(_A)
class _H3cHPEOCTemplateUniSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,100)));namedValues=NamedValues(*(('auto',1),('s10M',10),('s100M',100)))
_H3cHPEOCTemplateUniSpeed_Type.__name__=_C
_H3cHPEOCTemplateUniSpeed_Object=MibTableColumn
h3cHPEOCTemplateUniSpeed=_H3cHPEOCTemplateUniSpeed_Object((1,3,6,1,4,1,2011,10,2,84,3,2,1,2),_H3cHPEOCTemplateUniSpeed_Type())
h3cHPEOCTemplateUniSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateUniSpeed.setStatus(_A)
class _H3cHPEOCTemplateUniDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('full',1),('half',2),('auto',3)))
_H3cHPEOCTemplateUniDuplex_Type.__name__=_C
_H3cHPEOCTemplateUniDuplex_Object=MibTableColumn
h3cHPEOCTemplateUniDuplex=_H3cHPEOCTemplateUniDuplex_Object((1,3,6,1,4,1,2011,10,2,84,3,2,1,3),_H3cHPEOCTemplateUniDuplex_Type())
h3cHPEOCTemplateUniDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateUniDuplex.setStatus(_A)
class _H3cHPEOCTemplateUniPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cHPEOCTemplateUniPriority_Type.__name__=_C
_H3cHPEOCTemplateUniPriority_Object=MibTableColumn
h3cHPEOCTemplateUniPriority=_H3cHPEOCTemplateUniPriority_Object((1,3,6,1,4,1,2011,10,2,84,3,2,1,4),_H3cHPEOCTemplateUniPriority_Type())
h3cHPEOCTemplateUniPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateUniPriority.setStatus(_A)
class _H3cHPEOCTemplateUniFlowControl_Type(TruthValue):defaultValue=2
_H3cHPEOCTemplateUniFlowControl_Type.__name__=_I
_H3cHPEOCTemplateUniFlowControl_Object=MibTableColumn
h3cHPEOCTemplateUniFlowControl=_H3cHPEOCTemplateUniFlowControl_Object((1,3,6,1,4,1,2011,10,2,84,3,2,1,5),_H3cHPEOCTemplateUniFlowControl_Type())
h3cHPEOCTemplateUniFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateUniFlowControl.setStatus(_A)
_H3cHPEOCTemplateUniUpLineRate_Type=Unsigned32
_H3cHPEOCTemplateUniUpLineRate_Object=MibTableColumn
h3cHPEOCTemplateUniUpLineRate=_H3cHPEOCTemplateUniUpLineRate_Object((1,3,6,1,4,1,2011,10,2,84,3,2,1,6),_H3cHPEOCTemplateUniUpLineRate_Type())
h3cHPEOCTemplateUniUpLineRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateUniUpLineRate.setStatus(_A)
_H3cHPEOCTemplateUniDownLineRate_Type=Unsigned32
_H3cHPEOCTemplateUniDownLineRate_Object=MibTableColumn
h3cHPEOCTemplateUniDownLineRate=_H3cHPEOCTemplateUniDownLineRate_Object((1,3,6,1,4,1,2011,10,2,84,3,2,1,7),_H3cHPEOCTemplateUniDownLineRate_Type())
h3cHPEOCTemplateUniDownLineRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateUniDownLineRate.setStatus(_A)
class _H3cHPEOCTemplateUniAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_H3cHPEOCTemplateUniAdminStatus_Type.__name__=_C
_H3cHPEOCTemplateUniAdminStatus_Object=MibTableColumn
h3cHPEOCTemplateUniAdminStatus=_H3cHPEOCTemplateUniAdminStatus_Object((1,3,6,1,4,1,2011,10,2,84,3,2,1,8),_H3cHPEOCTemplateUniAdminStatus_Type())
h3cHPEOCTemplateUniAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateUniAdminStatus.setStatus(_A)
class _H3cHPEOCTemplateUniVLANType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('access',1),('trunk',2),('hybrid',3)))
_H3cHPEOCTemplateUniVLANType_Type.__name__=_C
_H3cHPEOCTemplateUniVLANType_Object=MibTableColumn
h3cHPEOCTemplateUniVLANType=_H3cHPEOCTemplateUniVLANType_Object((1,3,6,1,4,1,2011,10,2,84,3,2,1,9),_H3cHPEOCTemplateUniVLANType_Type())
h3cHPEOCTemplateUniVLANType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateUniVLANType.setStatus(_A)
class _H3cHPEOCTemplateUniPvid_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cHPEOCTemplateUniPvid_Type.__name__=_C
_H3cHPEOCTemplateUniPvid_Object=MibTableColumn
h3cHPEOCTemplateUniPvid=_H3cHPEOCTemplateUniPvid_Object((1,3,6,1,4,1,2011,10,2,84,3,2,1,10),_H3cHPEOCTemplateUniPvid_Type())
h3cHPEOCTemplateUniPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateUniPvid.setStatus(_A)
class _H3cHPEOCTemplateUniVlanTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tagged',1),('untagged',2)))
_H3cHPEOCTemplateUniVlanTag_Type.__name__=_C
_H3cHPEOCTemplateUniVlanTag_Object=MibTableColumn
h3cHPEOCTemplateUniVlanTag=_H3cHPEOCTemplateUniVlanTag_Object((1,3,6,1,4,1,2011,10,2,84,3,2,1,11),_H3cHPEOCTemplateUniVlanTag_Type())
h3cHPEOCTemplateUniVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCTemplateUniVlanTag.setStatus(_A)
_H3cHPEOCCnuAccess_ObjectIdentity=ObjectIdentity
h3cHPEOCCnuAccess=_H3cHPEOCCnuAccess_ObjectIdentity((1,3,6,1,4,1,2011,10,2,84,4))
_H3cHPEOCCnuAccessTable_Object=MibTable
h3cHPEOCCnuAccessTable=_H3cHPEOCCnuAccessTable_Object((1,3,6,1,4,1,2011,10,2,84,4,1))
if mibBuilder.loadTexts:h3cHPEOCCnuAccessTable.setStatus(_A)
_H3cHPEOCCnuAccessEntry_Object=MibTableRow
h3cHPEOCCnuAccessEntry=_H3cHPEOCCnuAccessEntry_Object((1,3,6,1,4,1,2011,10,2,84,4,1,1))
h3cHPEOCCnuAccessEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:h3cHPEOCCnuAccessEntry.setStatus(_A)
_H3cHPEOCCnuAccessIndex_Type=Integer32
_H3cHPEOCCnuAccessIndex_Object=MibTableColumn
h3cHPEOCCnuAccessIndex=_H3cHPEOCCnuAccessIndex_Object((1,3,6,1,4,1,2011,10,2,84,4,1,1,1),_H3cHPEOCCnuAccessIndex_Type())
h3cHPEOCCnuAccessIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cHPEOCCnuAccessIndex.setStatus(_A)
_H3cHPEOCCnuHFID_Type=DisplayString
_H3cHPEOCCnuHFID_Object=MibTableColumn
h3cHPEOCCnuHFID=_H3cHPEOCCnuHFID_Object((1,3,6,1,4,1,2011,10,2,84,4,1,1,2),_H3cHPEOCCnuHFID_Type())
h3cHPEOCCnuHFID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCCnuHFID.setStatus(_A)
_H3cHPEOCManuInfo_Type=DisplayString
_H3cHPEOCManuInfo_Object=MibTableColumn
h3cHPEOCManuInfo=_H3cHPEOCManuInfo_Object((1,3,6,1,4,1,2011,10,2,84,4,1,1,3),_H3cHPEOCManuInfo_Type())
h3cHPEOCManuInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCManuInfo.setStatus(_A)
class _H3cHPEOCCnuType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cHPEOCCnuType_Type.__name__=_C
_H3cHPEOCCnuType_Object=MibTableColumn
h3cHPEOCCnuType=_H3cHPEOCCnuType_Object((1,3,6,1,4,1,2011,10,2,84,4,1,1,4),_H3cHPEOCCnuType_Type())
h3cHPEOCCnuType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCCnuType.setStatus(_A)
class _H3cHPEOCCnuSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rtl8306e',1),('ar8236',2),('mv6061',3),('mv6031',4)))
_H3cHPEOCCnuSwitchType_Type.__name__=_C
_H3cHPEOCCnuSwitchType_Object=MibTableColumn
h3cHPEOCCnuSwitchType=_H3cHPEOCCnuSwitchType_Object((1,3,6,1,4,1,2011,10,2,84,4,1,1,5),_H3cHPEOCCnuSwitchType_Type())
h3cHPEOCCnuSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCCnuSwitchType.setStatus(_A)
_H3cHPEOCCnuUniNum_Type=Integer32
_H3cHPEOCCnuUniNum_Object=MibTableColumn
h3cHPEOCCnuUniNum=_H3cHPEOCCnuUniNum_Object((1,3,6,1,4,1,2011,10,2,84,4,1,1,6),_H3cHPEOCCnuUniNum_Type())
h3cHPEOCCnuUniNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCCnuUniNum.setStatus(_A)
_H3cHPEOCCnuPhy2Uni_Type=OctetString
_H3cHPEOCCnuPhy2Uni_Object=MibTableColumn
h3cHPEOCCnuPhy2Uni=_H3cHPEOCCnuPhy2Uni_Object((1,3,6,1,4,1,2011,10,2,84,4,1,1,7),_H3cHPEOCCnuPhy2Uni_Type())
h3cHPEOCCnuPhy2Uni.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cHPEOCCnuPhy2Uni.setStatus(_A)
_H3cHPEOCCnuAccessRowStatus_Type=RowStatus
_H3cHPEOCCnuAccessRowStatus_Object=MibTableColumn
h3cHPEOCCnuAccessRowStatus=_H3cHPEOCCnuAccessRowStatus_Object((1,3,6,1,4,1,2011,10,2,84,4,1,1,8),_H3cHPEOCCnuAccessRowStatus_Type())
h3cHPEOCCnuAccessRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cHPEOCCnuAccessRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'h3cHPEOC':h3cHPEOC,'h3cHPEOCSystem':h3cHPEOCSystem,'h3cHPEOCCltVlanType':h3cHPEOCCltVlanType,'h3cHPEOCCltVlanManTable':h3cHPEOCCltVlanManTable,'h3cHPEOCCltVlanManEntry':h3cHPEOCCltVlanManEntry,'h3cHPEOCCltEthPortType':h3cHPEOCCltEthPortType,'h3cHPEOCCltSysManTable':h3cHPEOCCltSysManTable,'h3cHPEOCCltSysManEntry':h3cHPEOCCltSysManEntry,'h3cHPEOCCltDescr':h3cHPEOCCltDescr,'h3cHPEOCCltFwVersion':h3cHPEOCCltFwVersion,'h3cHPEOCCltLinkState':h3cHPEOCCltLinkState,'h3cHPEOCCnuSysManTable':h3cHPEOCCnuSysManTable,'h3cHPEOCCnuSysManEntry':h3cHPEOCCnuSysManEntry,'h3cHPEOCCnuBcastControl':h3cHPEOCCnuBcastControl,'h3cHPEOCCnuAnonymStatus':h3cHPEOCCnuAnonymStatus,'h3cHPEOCCnuMacLimit':h3cHPEOCCnuMacLimit,'h3cHPEOCCltAutoUpgrade':h3cHPEOCCltAutoUpgrade,'h3cHPEOCOnLineCnuNumber':h3cHPEOCOnLineCnuNumber,'h3cHPEOCCpuMacAddress':h3cHPEOCCpuMacAddress,'h3cHPEOCOffLineCnuNumber':h3cHPEOCOffLineCnuNumber,'h3cHPEOCDownLoadCNUFWResult':h3cHPEOCDownLoadCNUFWResult,'h3cHPEOCCltAutoUpgradeType':h3cHPEOCCltAutoUpgradeType,'h3cHPEOCAutoUpObjects':h3cHPEOCAutoUpObjects,'h3cHPEOCServerAddress':h3cHPEOCServerAddress,'h3cHPEOCServerUser':h3cHPEOCServerUser,'h3cHPEOCServerPassword':h3cHPEOCServerPassword,'h3cHPEOCCltLoopbackDetect':h3cHPEOCCltLoopbackDetect,'h3cHPEOCTemplateEnable':h3cHPEOCTemplateEnable,'h3cHPEOCCableInfo':h3cHPEOCCableInfo,'h3cHPEOCCableInfoTable':h3cHPEOCCableInfoTable,'h3cHPEOCCableInfoEntry':h3cHPEOCCableInfoEntry,'h3cHPEOCFECErrors':h3cHPEOCFECErrors,'h3cHPEOCAvgBitsPerCarrier':h3cHPEOCAvgBitsPerCarrier,'h3cHPEOCAvgSNRPerCarrier':h3cHPEOCAvgSNRPerCarrier,'h3cHPEOCAvgInPBCRCErrors':h3cHPEOCAvgInPBCRCErrors,'h3cHPEOCInTotalPkts':h3cHPEOCInTotalPkts,'h3cHPEOCAvgOutPower':h3cHPEOCAvgOutPower,'h3cHPEOCAvgOutPBCRCErrors':h3cHPEOCAvgOutPBCRCErrors,'h3cHPEOCOutTotalPkts':h3cHPEOCOutTotalPkts,'h3cHPEOCBitPerSymbolTable':h3cHPEOCBitPerSymbolTable,'h3cHPEOCBitPerSymbolEntry':h3cHPEOCBitPerSymbolEntry,_L:h3cHPEOCBitPerSymbolIndex,'h3cHPEOCBitPerSymbol':h3cHPEOCBitPerSymbol,'h3cHPEOCTemplate':h3cHPEOCTemplate,'h3cHPEOCTemplateGlobalTable':h3cHPEOCTemplateGlobalTable,'h3cHPEOCTemplateGlobalEntry':h3cHPEOCTemplateGlobalEntry,_J:h3cHPEOCTemplateIndex,'h3cHPEOCTemplateType':h3cHPEOCTemplateType,'h3cHPEOCTemplateName':h3cHPEOCTemplateName,'h3cHPEOCTemplateDescr':h3cHPEOCTemplateDescr,'h3cHPEOCTemplateCnuMaxDownBW':h3cHPEOCTemplateCnuMaxDownBW,'h3cHPEOCTemplateCnuMaxUpBW':h3cHPEOCTemplateCnuMaxUpBW,'h3cHPEOCTemplateCnuBcastControl':h3cHPEOCTemplateCnuBcastControl,'h3cHPEOCTemplateCnuMacLimit':h3cHPEOCTemplateCnuMacLimit,'h3cHPEOCTemplateCb201VlanEn':h3cHPEOCTemplateCb201VlanEn,'h3cHPEOCTemplateRowStatus':h3cHPEOCTemplateRowStatus,'h3cHPEOCTemplateSwitchTable':h3cHPEOCTemplateSwitchTable,'h3cHPEOCTemplateSwitchEntry':h3cHPEOCTemplateSwitchEntry,_P:h3cHPEOCTemplateUniIndex,'h3cHPEOCTemplateUniSpeed':h3cHPEOCTemplateUniSpeed,'h3cHPEOCTemplateUniDuplex':h3cHPEOCTemplateUniDuplex,'h3cHPEOCTemplateUniPriority':h3cHPEOCTemplateUniPriority,'h3cHPEOCTemplateUniFlowControl':h3cHPEOCTemplateUniFlowControl,'h3cHPEOCTemplateUniUpLineRate':h3cHPEOCTemplateUniUpLineRate,'h3cHPEOCTemplateUniDownLineRate':h3cHPEOCTemplateUniDownLineRate,'h3cHPEOCTemplateUniAdminStatus':h3cHPEOCTemplateUniAdminStatus,'h3cHPEOCTemplateUniVLANType':h3cHPEOCTemplateUniVLANType,'h3cHPEOCTemplateUniPvid':h3cHPEOCTemplateUniPvid,'h3cHPEOCTemplateUniVlanTag':h3cHPEOCTemplateUniVlanTag,'h3cHPEOCCnuAccess':h3cHPEOCCnuAccess,'h3cHPEOCCnuAccessTable':h3cHPEOCCnuAccessTable,'h3cHPEOCCnuAccessEntry':h3cHPEOCCnuAccessEntry,_Q:h3cHPEOCCnuAccessIndex,'h3cHPEOCCnuHFID':h3cHPEOCCnuHFID,'h3cHPEOCManuInfo':h3cHPEOCManuInfo,'h3cHPEOCCnuType':h3cHPEOCCnuType,'h3cHPEOCCnuSwitchType':h3cHPEOCCnuSwitchType,'h3cHPEOCCnuUniNum':h3cHPEOCCnuUniNum,'h3cHPEOCCnuPhy2Uni':h3cHPEOCCnuPhy2Uni,'h3cHPEOCCnuAccessRowStatus':h3cHPEOCCnuAccessRowStatus})
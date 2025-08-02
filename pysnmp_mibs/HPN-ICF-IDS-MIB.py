_S='hpnicfIDSTrapCfgLineInFile'
_R='hpnicfIDSTrapUpgradeType'
_Q='hpnicfIDSTrapLoginType'
_P='hpnicfIDSTrapUserName'
_O='hpnicfIDSTrapCertName'
_N='hpnicfIDSTrapCRLName'
_M='hpnicfIDSTrapEngineID'
_L='hpnicfIDSTrapDetectRuleID'
_K='hpnicfIDSTrapStatSessionTabLen'
_J='hpnicfIDSTrapIPFragmentQueueLen'
_I='hpnicfIDSTrapFileName'
_H='hpnicfIDSTrapIPAddress'
_G='hpnicfIDSTrapIPAddressType'
_F='Integer32'
_E='OctetString'
_D='hpnicfIDSTrapReasonForError'
_C='accessible-for-notify'
_B='current'
_A='HPN-ICF-IDS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfIDSMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,47,1))
_HpnicfIds_ObjectIdentity=ObjectIdentity
hpnicfIds=_HpnicfIds_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,47))
_HpnicfIDSTrapGroup_ObjectIdentity=ObjectIdentity
hpnicfIDSTrapGroup=_HpnicfIDSTrapGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1))
_HpnicfIDSTrapInfo_ObjectIdentity=ObjectIdentity
hpnicfIDSTrapInfo=_HpnicfIDSTrapInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1))
_HpnicfIDSTrapIPFragmentQueueLen_Type=Unsigned32
_HpnicfIDSTrapIPFragmentQueueLen_Object=MibScalar
hpnicfIDSTrapIPFragmentQueueLen=_HpnicfIDSTrapIPFragmentQueueLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,1),_HpnicfIDSTrapIPFragmentQueueLen_Type())
hpnicfIDSTrapIPFragmentQueueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapIPFragmentQueueLen.setStatus(_B)
_HpnicfIDSTrapStatSessionTabLen_Type=Unsigned32
_HpnicfIDSTrapStatSessionTabLen_Object=MibScalar
hpnicfIDSTrapStatSessionTabLen=_HpnicfIDSTrapStatSessionTabLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,2),_HpnicfIDSTrapStatSessionTabLen_Type())
hpnicfIDSTrapStatSessionTabLen.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapStatSessionTabLen.setStatus(_B)
_HpnicfIDSTrapIPAddressType_Type=InetAddressType
_HpnicfIDSTrapIPAddressType_Object=MibScalar
hpnicfIDSTrapIPAddressType=_HpnicfIDSTrapIPAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,3),_HpnicfIDSTrapIPAddressType_Type())
hpnicfIDSTrapIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapIPAddressType.setStatus(_B)
_HpnicfIDSTrapIPAddress_Type=InetAddress
_HpnicfIDSTrapIPAddress_Object=MibScalar
hpnicfIDSTrapIPAddress=_HpnicfIDSTrapIPAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,4),_HpnicfIDSTrapIPAddress_Type())
hpnicfIDSTrapIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapIPAddress.setStatus(_B)
class _HpnicfIDSTrapUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfIDSTrapUserName_Type.__name__=_E
_HpnicfIDSTrapUserName_Object=MibScalar
hpnicfIDSTrapUserName=_HpnicfIDSTrapUserName_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,5),_HpnicfIDSTrapUserName_Type())
hpnicfIDSTrapUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapUserName.setStatus(_B)
class _HpnicfIDSTrapLoginType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('telnet',1),('ssh',2),('web',3)))
_HpnicfIDSTrapLoginType_Type.__name__=_F
_HpnicfIDSTrapLoginType_Object=MibScalar
hpnicfIDSTrapLoginType=_HpnicfIDSTrapLoginType_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,6),_HpnicfIDSTrapLoginType_Type())
hpnicfIDSTrapLoginType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapLoginType.setStatus(_B)
class _HpnicfIDSTrapUpgradeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('programme',1),('crb',2),('vrb',3)))
_HpnicfIDSTrapUpgradeType_Type.__name__=_F
_HpnicfIDSTrapUpgradeType_Object=MibScalar
hpnicfIDSTrapUpgradeType=_HpnicfIDSTrapUpgradeType_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,7),_HpnicfIDSTrapUpgradeType_Type())
hpnicfIDSTrapUpgradeType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapUpgradeType.setStatus(_B)
class _HpnicfIDSTrapCRLName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfIDSTrapCRLName_Type.__name__=_E
_HpnicfIDSTrapCRLName_Object=MibScalar
hpnicfIDSTrapCRLName=_HpnicfIDSTrapCRLName_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,8),_HpnicfIDSTrapCRLName_Type())
hpnicfIDSTrapCRLName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapCRLName.setStatus(_B)
class _HpnicfIDSTrapCertName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfIDSTrapCertName_Type.__name__=_E
_HpnicfIDSTrapCertName_Object=MibScalar
hpnicfIDSTrapCertName=_HpnicfIDSTrapCertName_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,9),_HpnicfIDSTrapCertName_Type())
hpnicfIDSTrapCertName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapCertName.setStatus(_B)
_HpnicfIDSTrapDetectRuleID_Type=Unsigned32
_HpnicfIDSTrapDetectRuleID_Object=MibScalar
hpnicfIDSTrapDetectRuleID=_HpnicfIDSTrapDetectRuleID_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,10),_HpnicfIDSTrapDetectRuleID_Type())
hpnicfIDSTrapDetectRuleID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapDetectRuleID.setStatus(_B)
_HpnicfIDSTrapEngineID_Type=Integer32
_HpnicfIDSTrapEngineID_Object=MibScalar
hpnicfIDSTrapEngineID=_HpnicfIDSTrapEngineID_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,11),_HpnicfIDSTrapEngineID_Type())
hpnicfIDSTrapEngineID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapEngineID.setStatus(_B)
class _HpnicfIDSTrapFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfIDSTrapFileName_Type.__name__=_E
_HpnicfIDSTrapFileName_Object=MibScalar
hpnicfIDSTrapFileName=_HpnicfIDSTrapFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,12),_HpnicfIDSTrapFileName_Type())
hpnicfIDSTrapFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapFileName.setStatus(_B)
_HpnicfIDSTrapCfgLineInFile_Type=Unsigned32
_HpnicfIDSTrapCfgLineInFile_Object=MibScalar
hpnicfIDSTrapCfgLineInFile=_HpnicfIDSTrapCfgLineInFile_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,13),_HpnicfIDSTrapCfgLineInFile_Type())
hpnicfIDSTrapCfgLineInFile.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapCfgLineInFile.setStatus(_B)
class _HpnicfIDSTrapReasonForError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfIDSTrapReasonForError_Type.__name__=_E
_HpnicfIDSTrapReasonForError_Object=MibScalar
hpnicfIDSTrapReasonForError=_HpnicfIDSTrapReasonForError_Object((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,1,14),_HpnicfIDSTrapReasonForError_Type())
hpnicfIDSTrapReasonForError.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIDSTrapReasonForError.setStatus(_B)
_HpnicfIDSTrap_ObjectIdentity=ObjectIdentity
hpnicfIDSTrap=_HpnicfIDSTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2))
_HpnicfIDSTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfIDSTrapPrefix=_HpnicfIDSTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0))
hpnicfIDSTrapIPFragQueueFull=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0,1))
hpnicfIDSTrapIPFragQueueFull.setObjects(*((_A,_J),(_A,_D)))
if mibBuilder.loadTexts:hpnicfIDSTrapIPFragQueueFull.setStatus(_B)
hpnicfIDSTrapStatSessTabFull=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0,2))
hpnicfIDSTrapStatSessTabFull.setObjects(*((_A,_K),(_A,_D)))
if mibBuilder.loadTexts:hpnicfIDSTrapStatSessTabFull.setStatus(_B)
hpnicfIDSTrapDetectRuleParseFail=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0,3))
hpnicfIDSTrapDetectRuleParseFail.setObjects(*((_A,_L),(_A,_M),(_A,_D)))
if mibBuilder.loadTexts:hpnicfIDSTrapDetectRuleParseFail.setStatus(_B)
hpnicfIDSTrapDBConnLost=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0,4))
hpnicfIDSTrapDBConnLost.setObjects(*((_A,_G),(_A,_H),(_A,_D)))
if mibBuilder.loadTexts:hpnicfIDSTrapDBConnLost.setStatus(_B)
hpnicfIDSTrapCRLNeedUpdate=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0,5))
hpnicfIDSTrapCRLNeedUpdate.setObjects(*((_A,_N),(_A,_D)))
if mibBuilder.loadTexts:hpnicfIDSTrapCRLNeedUpdate.setStatus(_B)
hpnicfIDSTrapCertOverdue=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0,6))
hpnicfIDSTrapCertOverdue.setObjects(*((_A,_O),(_A,_D)))
if mibBuilder.loadTexts:hpnicfIDSTrapCertOverdue.setStatus(_B)
hpnicfIDSTrapTooManyLoginFail=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0,7))
hpnicfIDSTrapTooManyLoginFail.setObjects(*((_A,_P),(_A,_G),(_A,_H),(_A,_Q),(_A,_D)))
if mibBuilder.loadTexts:hpnicfIDSTrapTooManyLoginFail.setStatus(_B)
hpnicfIDSTrapUpgradeError=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0,8))
hpnicfIDSTrapUpgradeError.setObjects(*((_A,_R),(_A,_D)))
if mibBuilder.loadTexts:hpnicfIDSTrapUpgradeError.setStatus(_B)
hpnicfIDSTrapFileAccessError=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0,9))
hpnicfIDSTrapFileAccessError.setObjects(*((_A,_I),(_A,_D)))
if mibBuilder.loadTexts:hpnicfIDSTrapFileAccessError.setStatus(_B)
hpnicfIDSTrapConsArithMemLow=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0,10))
hpnicfIDSTrapConsArithMemLow.setObjects((_A,_D))
if mibBuilder.loadTexts:hpnicfIDSTrapConsArithMemLow.setStatus(_B)
hpnicfIDSTrapSSRAMOperFail=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0,11))
hpnicfIDSTrapSSRAMOperFail.setObjects((_A,_D))
if mibBuilder.loadTexts:hpnicfIDSTrapSSRAMOperFail.setStatus(_B)
hpnicfIDSTrapPacketProcessDisorder=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0,12))
hpnicfIDSTrapPacketProcessDisorder.setObjects((_A,_D))
if mibBuilder.loadTexts:hpnicfIDSTrapPacketProcessDisorder.setStatus(_B)
hpnicfIDSTrapCfgFileFormatError=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,47,1,1,2,0,13))
hpnicfIDSTrapCfgFileFormatError.setObjects(*((_A,_I),(_A,_S)))
if mibBuilder.loadTexts:hpnicfIDSTrapCfgFileFormatError.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpnicfIds':hpnicfIds,'hpnicfIDSMib':hpnicfIDSMib,'hpnicfIDSTrapGroup':hpnicfIDSTrapGroup,'hpnicfIDSTrapInfo':hpnicfIDSTrapInfo,_J:hpnicfIDSTrapIPFragmentQueueLen,_K:hpnicfIDSTrapStatSessionTabLen,_G:hpnicfIDSTrapIPAddressType,_H:hpnicfIDSTrapIPAddress,_P:hpnicfIDSTrapUserName,_Q:hpnicfIDSTrapLoginType,_R:hpnicfIDSTrapUpgradeType,_N:hpnicfIDSTrapCRLName,_O:hpnicfIDSTrapCertName,_L:hpnicfIDSTrapDetectRuleID,_M:hpnicfIDSTrapEngineID,_I:hpnicfIDSTrapFileName,_S:hpnicfIDSTrapCfgLineInFile,_D:hpnicfIDSTrapReasonForError,'hpnicfIDSTrap':hpnicfIDSTrap,'hpnicfIDSTrapPrefix':hpnicfIDSTrapPrefix,'hpnicfIDSTrapIPFragQueueFull':hpnicfIDSTrapIPFragQueueFull,'hpnicfIDSTrapStatSessTabFull':hpnicfIDSTrapStatSessTabFull,'hpnicfIDSTrapDetectRuleParseFail':hpnicfIDSTrapDetectRuleParseFail,'hpnicfIDSTrapDBConnLost':hpnicfIDSTrapDBConnLost,'hpnicfIDSTrapCRLNeedUpdate':hpnicfIDSTrapCRLNeedUpdate,'hpnicfIDSTrapCertOverdue':hpnicfIDSTrapCertOverdue,'hpnicfIDSTrapTooManyLoginFail':hpnicfIDSTrapTooManyLoginFail,'hpnicfIDSTrapUpgradeError':hpnicfIDSTrapUpgradeError,'hpnicfIDSTrapFileAccessError':hpnicfIDSTrapFileAccessError,'hpnicfIDSTrapConsArithMemLow':hpnicfIDSTrapConsArithMemLow,'hpnicfIDSTrapSSRAMOperFail':hpnicfIDSTrapSSRAMOperFail,'hpnicfIDSTrapPacketProcessDisorder':hpnicfIDSTrapPacketProcessDisorder,'hpnicfIDSTrapCfgFileFormatError':hpnicfIDSTrapCfgFileFormatError})
_S='h3cIDSTrapCfgLineInFile'
_R='h3cIDSTrapUpgradeType'
_Q='h3cIDSTrapLoginType'
_P='h3cIDSTrapUserName'
_O='h3cIDSTrapCertName'
_N='h3cIDSTrapCRLName'
_M='h3cIDSTrapEngineID'
_L='h3cIDSTrapDetectRuleID'
_K='h3cIDSTrapStatSessionTabLen'
_J='h3cIDSTrapIPFragmentQueueLen'
_I='h3cIDSTrapFileName'
_H='h3cIDSTrapIPAddress'
_G='h3cIDSTrapIPAddressType'
_F='Integer32'
_E='OctetString'
_D='h3cIDSTrapReasonForError'
_C='accessible-for-notify'
_B='current'
_A='A3COM-HUAWEI-IDS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cIDSMib=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,47,1))
_H3cIds_ObjectIdentity=ObjectIdentity
h3cIds=_H3cIds_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,47))
_H3cIDSTrapGroup_ObjectIdentity=ObjectIdentity
h3cIDSTrapGroup=_H3cIDSTrapGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,47,1,1))
_H3cIDSTrapInfo_ObjectIdentity=ObjectIdentity
h3cIDSTrapInfo=_H3cIDSTrapInfo_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1))
_H3cIDSTrapIPFragmentQueueLen_Type=Unsigned32
_H3cIDSTrapIPFragmentQueueLen_Object=MibScalar
h3cIDSTrapIPFragmentQueueLen=_H3cIDSTrapIPFragmentQueueLen_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,1),_H3cIDSTrapIPFragmentQueueLen_Type())
h3cIDSTrapIPFragmentQueueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapIPFragmentQueueLen.setStatus(_B)
_H3cIDSTrapStatSessionTabLen_Type=Unsigned32
_H3cIDSTrapStatSessionTabLen_Object=MibScalar
h3cIDSTrapStatSessionTabLen=_H3cIDSTrapStatSessionTabLen_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,2),_H3cIDSTrapStatSessionTabLen_Type())
h3cIDSTrapStatSessionTabLen.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapStatSessionTabLen.setStatus(_B)
_H3cIDSTrapIPAddressType_Type=InetAddressType
_H3cIDSTrapIPAddressType_Object=MibScalar
h3cIDSTrapIPAddressType=_H3cIDSTrapIPAddressType_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,3),_H3cIDSTrapIPAddressType_Type())
h3cIDSTrapIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapIPAddressType.setStatus(_B)
_H3cIDSTrapIPAddress_Type=InetAddress
_H3cIDSTrapIPAddress_Object=MibScalar
h3cIDSTrapIPAddress=_H3cIDSTrapIPAddress_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,4),_H3cIDSTrapIPAddress_Type())
h3cIDSTrapIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapIPAddress.setStatus(_B)
class _H3cIDSTrapUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cIDSTrapUserName_Type.__name__=_E
_H3cIDSTrapUserName_Object=MibScalar
h3cIDSTrapUserName=_H3cIDSTrapUserName_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,5),_H3cIDSTrapUserName_Type())
h3cIDSTrapUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapUserName.setStatus(_B)
class _H3cIDSTrapLoginType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('telnet',1),('ssh',2),('web',3)))
_H3cIDSTrapLoginType_Type.__name__=_F
_H3cIDSTrapLoginType_Object=MibScalar
h3cIDSTrapLoginType=_H3cIDSTrapLoginType_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,6),_H3cIDSTrapLoginType_Type())
h3cIDSTrapLoginType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapLoginType.setStatus(_B)
class _H3cIDSTrapUpgradeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('programme',1),('crb',2),('vrb',3)))
_H3cIDSTrapUpgradeType_Type.__name__=_F
_H3cIDSTrapUpgradeType_Object=MibScalar
h3cIDSTrapUpgradeType=_H3cIDSTrapUpgradeType_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,7),_H3cIDSTrapUpgradeType_Type())
h3cIDSTrapUpgradeType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapUpgradeType.setStatus(_B)
class _H3cIDSTrapCRLName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cIDSTrapCRLName_Type.__name__=_E
_H3cIDSTrapCRLName_Object=MibScalar
h3cIDSTrapCRLName=_H3cIDSTrapCRLName_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,8),_H3cIDSTrapCRLName_Type())
h3cIDSTrapCRLName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapCRLName.setStatus(_B)
class _H3cIDSTrapCertName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cIDSTrapCertName_Type.__name__=_E
_H3cIDSTrapCertName_Object=MibScalar
h3cIDSTrapCertName=_H3cIDSTrapCertName_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,9),_H3cIDSTrapCertName_Type())
h3cIDSTrapCertName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapCertName.setStatus(_B)
_H3cIDSTrapDetectRuleID_Type=Unsigned32
_H3cIDSTrapDetectRuleID_Object=MibScalar
h3cIDSTrapDetectRuleID=_H3cIDSTrapDetectRuleID_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,10),_H3cIDSTrapDetectRuleID_Type())
h3cIDSTrapDetectRuleID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapDetectRuleID.setStatus(_B)
_H3cIDSTrapEngineID_Type=Integer32
_H3cIDSTrapEngineID_Object=MibScalar
h3cIDSTrapEngineID=_H3cIDSTrapEngineID_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,11),_H3cIDSTrapEngineID_Type())
h3cIDSTrapEngineID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapEngineID.setStatus(_B)
class _H3cIDSTrapFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_H3cIDSTrapFileName_Type.__name__=_E
_H3cIDSTrapFileName_Object=MibScalar
h3cIDSTrapFileName=_H3cIDSTrapFileName_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,12),_H3cIDSTrapFileName_Type())
h3cIDSTrapFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapFileName.setStatus(_B)
_H3cIDSTrapCfgLineInFile_Type=Unsigned32
_H3cIDSTrapCfgLineInFile_Object=MibScalar
h3cIDSTrapCfgLineInFile=_H3cIDSTrapCfgLineInFile_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,13),_H3cIDSTrapCfgLineInFile_Type())
h3cIDSTrapCfgLineInFile.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapCfgLineInFile.setStatus(_B)
class _H3cIDSTrapReasonForError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_H3cIDSTrapReasonForError_Type.__name__=_E
_H3cIDSTrapReasonForError_Object=MibScalar
h3cIDSTrapReasonForError=_H3cIDSTrapReasonForError_Object((1,3,6,1,4,1,43,45,1,10,2,47,1,1,1,14),_H3cIDSTrapReasonForError_Type())
h3cIDSTrapReasonForError.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIDSTrapReasonForError.setStatus(_B)
_H3cIDSTrap_ObjectIdentity=ObjectIdentity
h3cIDSTrap=_H3cIDSTrap_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2))
_H3cIDSTrapPrefix_ObjectIdentity=ObjectIdentity
h3cIDSTrapPrefix=_H3cIDSTrapPrefix_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0))
h3cIDSTrapIPFragQueueFull=NotificationType((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0,1))
h3cIDSTrapIPFragQueueFull.setObjects(*((_A,_J),(_A,_D)))
if mibBuilder.loadTexts:h3cIDSTrapIPFragQueueFull.setStatus(_B)
h3cIDSTrapStatSessTabFull=NotificationType((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0,2))
h3cIDSTrapStatSessTabFull.setObjects(*((_A,_K),(_A,_D)))
if mibBuilder.loadTexts:h3cIDSTrapStatSessTabFull.setStatus(_B)
h3cIDSTrapDetectRuleParseFail=NotificationType((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0,3))
h3cIDSTrapDetectRuleParseFail.setObjects(*((_A,_L),(_A,_M),(_A,_D)))
if mibBuilder.loadTexts:h3cIDSTrapDetectRuleParseFail.setStatus(_B)
h3cIDSTrapDBConnLost=NotificationType((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0,4))
h3cIDSTrapDBConnLost.setObjects(*((_A,_G),(_A,_H),(_A,_D)))
if mibBuilder.loadTexts:h3cIDSTrapDBConnLost.setStatus(_B)
h3cIDSTrapCRLNeedUpdate=NotificationType((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0,5))
h3cIDSTrapCRLNeedUpdate.setObjects(*((_A,_N),(_A,_D)))
if mibBuilder.loadTexts:h3cIDSTrapCRLNeedUpdate.setStatus(_B)
h3cIDSTrapCertOverdue=NotificationType((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0,6))
h3cIDSTrapCertOverdue.setObjects(*((_A,_O),(_A,_D)))
if mibBuilder.loadTexts:h3cIDSTrapCertOverdue.setStatus(_B)
h3cIDSTrapTooManyLoginFail=NotificationType((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0,7))
h3cIDSTrapTooManyLoginFail.setObjects(*((_A,_P),(_A,_G),(_A,_H),(_A,_Q),(_A,_D)))
if mibBuilder.loadTexts:h3cIDSTrapTooManyLoginFail.setStatus(_B)
h3cIDSTrapUpgradeError=NotificationType((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0,8))
h3cIDSTrapUpgradeError.setObjects(*((_A,_R),(_A,_D)))
if mibBuilder.loadTexts:h3cIDSTrapUpgradeError.setStatus(_B)
h3cIDSTrapFileAccessError=NotificationType((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0,9))
h3cIDSTrapFileAccessError.setObjects(*((_A,_I),(_A,_D)))
if mibBuilder.loadTexts:h3cIDSTrapFileAccessError.setStatus(_B)
h3cIDSTrapConsArithMemLow=NotificationType((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0,10))
h3cIDSTrapConsArithMemLow.setObjects((_A,_D))
if mibBuilder.loadTexts:h3cIDSTrapConsArithMemLow.setStatus(_B)
h3cIDSTrapSSRAMOperFail=NotificationType((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0,11))
h3cIDSTrapSSRAMOperFail.setObjects((_A,_D))
if mibBuilder.loadTexts:h3cIDSTrapSSRAMOperFail.setStatus(_B)
h3cIDSTrapPacketProcessDisorder=NotificationType((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0,12))
h3cIDSTrapPacketProcessDisorder.setObjects((_A,_D))
if mibBuilder.loadTexts:h3cIDSTrapPacketProcessDisorder.setStatus(_B)
h3cIDSTrapCfgFileFormatError=NotificationType((1,3,6,1,4,1,43,45,1,10,2,47,1,1,2,0,13))
h3cIDSTrapCfgFileFormatError.setObjects(*((_A,_I),(_A,_S)))
if mibBuilder.loadTexts:h3cIDSTrapCfgFileFormatError.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'h3cIds':h3cIds,'h3cIDSMib':h3cIDSMib,'h3cIDSTrapGroup':h3cIDSTrapGroup,'h3cIDSTrapInfo':h3cIDSTrapInfo,_J:h3cIDSTrapIPFragmentQueueLen,_K:h3cIDSTrapStatSessionTabLen,_G:h3cIDSTrapIPAddressType,_H:h3cIDSTrapIPAddress,_P:h3cIDSTrapUserName,_Q:h3cIDSTrapLoginType,_R:h3cIDSTrapUpgradeType,_N:h3cIDSTrapCRLName,_O:h3cIDSTrapCertName,_L:h3cIDSTrapDetectRuleID,_M:h3cIDSTrapEngineID,_I:h3cIDSTrapFileName,_S:h3cIDSTrapCfgLineInFile,_D:h3cIDSTrapReasonForError,'h3cIDSTrap':h3cIDSTrap,'h3cIDSTrapPrefix':h3cIDSTrapPrefix,'h3cIDSTrapIPFragQueueFull':h3cIDSTrapIPFragQueueFull,'h3cIDSTrapStatSessTabFull':h3cIDSTrapStatSessTabFull,'h3cIDSTrapDetectRuleParseFail':h3cIDSTrapDetectRuleParseFail,'h3cIDSTrapDBConnLost':h3cIDSTrapDBConnLost,'h3cIDSTrapCRLNeedUpdate':h3cIDSTrapCRLNeedUpdate,'h3cIDSTrapCertOverdue':h3cIDSTrapCertOverdue,'h3cIDSTrapTooManyLoginFail':h3cIDSTrapTooManyLoginFail,'h3cIDSTrapUpgradeError':h3cIDSTrapUpgradeError,'h3cIDSTrapFileAccessError':h3cIDSTrapFileAccessError,'h3cIDSTrapConsArithMemLow':h3cIDSTrapConsArithMemLow,'h3cIDSTrapSSRAMOperFail':h3cIDSTrapSSRAMOperFail,'h3cIDSTrapPacketProcessDisorder':h3cIDSTrapPacketProcessDisorder,'h3cIDSTrapCfgFileFormatError':h3cIDSTrapCfgFileFormatError})
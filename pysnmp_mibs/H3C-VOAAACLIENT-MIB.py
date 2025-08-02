_H='h3cVoAAAGwAccessNumber'
_G='H3C-VOAAACLIENT-MIB'
_F='OctetString'
_E='read-write'
_D='Integer32'
_C='TruthValue'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cVoice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cVoice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_C)
h3cVoiceAAAClient=ModuleIdentity((1,3,6,1,4,1,2011,10,2,39,9))
if mibBuilder.loadTexts:h3cVoiceAAAClient.setRevisions(('2006-03-27 00:00',))
_H3cVoAAAClientObjects_ObjectIdentity=ObjectIdentity
h3cVoAAAClientObjects=_H3cVoAAAClientObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,39,9,1))
_H3cVoAAAClientCfgObjects_ObjectIdentity=ObjectIdentity
h3cVoAAAClientCfgObjects=_H3cVoAAAClientCfgObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,39,9,1,1))
class _H3cVoAAAGwAuthenDid_Type(TruthValue):defaultValue=2
_H3cVoAAAGwAuthenDid_Type.__name__=_C
_H3cVoAAAGwAuthenDid_Object=MibScalar
h3cVoAAAGwAuthenDid=_H3cVoAAAGwAuthenDid_Object((1,3,6,1,4,1,2011,10,2,39,9,1,1,1),_H3cVoAAAGwAuthenDid_Type())
h3cVoAAAGwAuthenDid.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cVoAAAGwAuthenDid.setStatus(_A)
class _H3cVoAAAGwAuthorDid_Type(TruthValue):defaultValue=2
_H3cVoAAAGwAuthorDid_Type.__name__=_C
_H3cVoAAAGwAuthorDid_Object=MibScalar
h3cVoAAAGwAuthorDid=_H3cVoAAAGwAuthorDid_Object((1,3,6,1,4,1,2011,10,2,39,9,1,1,2),_H3cVoAAAGwAuthorDid_Type())
h3cVoAAAGwAuthorDid.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cVoAAAGwAuthorDid.setStatus(_A)
class _H3cVoAAAGwAccountingDid_Type(TruthValue):defaultValue=2
_H3cVoAAAGwAccountingDid_Type.__name__=_C
_H3cVoAAAGwAccountingDid_Object=MibScalar
h3cVoAAAGwAccountingDid=_H3cVoAAAGwAccountingDid_Object((1,3,6,1,4,1,2011,10,2,39,9,1,1,3),_H3cVoAAAGwAccountingDid_Type())
h3cVoAAAGwAccountingDid.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cVoAAAGwAccountingDid.setStatus(_A)
class _H3cVoAAAGwAccountMethod_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('startAck',1),('startNoAck',2),('stopOnly',3)))
_H3cVoAAAGwAccountMethod_Type.__name__=_D
_H3cVoAAAGwAccountMethod_Object=MibScalar
h3cVoAAAGwAccountMethod=_H3cVoAAAGwAccountMethod_Object((1,3,6,1,4,1,2011,10,2,39,9,1,1,4),_H3cVoAAAGwAccountMethod_Type())
h3cVoAAAGwAccountMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cVoAAAGwAccountMethod.setStatus(_A)
_H3cVoAAAGwAccessNumberTable_Object=MibTable
h3cVoAAAGwAccessNumberTable=_H3cVoAAAGwAccessNumberTable_Object((1,3,6,1,4,1,2011,10,2,39,9,1,2))
if mibBuilder.loadTexts:h3cVoAAAGwAccessNumberTable.setStatus(_A)
_H3cVoAAAGwAccessNumberEntry_Object=MibTableRow
h3cVoAAAGwAccessNumberEntry=_H3cVoAAAGwAccessNumberEntry_Object((1,3,6,1,4,1,2011,10,2,39,9,1,2,1))
h3cVoAAAGwAccessNumberEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cVoAAAGwAccessNumberEntry.setStatus(_A)
class _H3cVoAAAGwAccessNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cVoAAAGwAccessNumber_Type.__name__=_F
_H3cVoAAAGwAccessNumber_Object=MibTableColumn
h3cVoAAAGwAccessNumber=_H3cVoAAAGwAccessNumber_Object((1,3,6,1,4,1,2011,10,2,39,9,1,2,1,1),_H3cVoAAAGwAccessNumber_Type())
h3cVoAAAGwAccessNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cVoAAAGwAccessNumber.setStatus(_A)
class _H3cVoAAAGwAuthentication_Type(TruthValue):defaultValue=2
_H3cVoAAAGwAuthentication_Type.__name__=_C
_H3cVoAAAGwAuthentication_Object=MibTableColumn
h3cVoAAAGwAuthentication=_H3cVoAAAGwAuthentication_Object((1,3,6,1,4,1,2011,10,2,39,9,1,2,1,2),_H3cVoAAAGwAuthentication_Type())
h3cVoAAAGwAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAAAGwAuthentication.setStatus(_A)
class _H3cVoAAAGwAuthorization_Type(TruthValue):defaultValue=2
_H3cVoAAAGwAuthorization_Type.__name__=_C
_H3cVoAAAGwAuthorization_Object=MibTableColumn
h3cVoAAAGwAuthorization=_H3cVoAAAGwAuthorization_Object((1,3,6,1,4,1,2011,10,2,39,9,1,2,1,3),_H3cVoAAAGwAuthorization_Type())
h3cVoAAAGwAuthorization.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAAAGwAuthorization.setStatus(_A)
class _H3cVoAAAGwAccounting_Type(TruthValue):defaultValue=2
_H3cVoAAAGwAccounting_Type.__name__=_C
_H3cVoAAAGwAccounting_Object=MibTableColumn
h3cVoAAAGwAccounting=_H3cVoAAAGwAccounting_Object((1,3,6,1,4,1,2011,10,2,39,9,1,2,1,4),_H3cVoAAAGwAccounting_Type())
h3cVoAAAGwAccounting.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAAAGwAccounting.setStatus(_A)
class _H3cVoAAAGwProcessConfig_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('callerNumber',1),('cardNumber',2),('callerNumIvr',3)))
_H3cVoAAAGwProcessConfig_Type.__name__=_D
_H3cVoAAAGwProcessConfig_Object=MibTableColumn
h3cVoAAAGwProcessConfig=_H3cVoAAAGwProcessConfig_Object((1,3,6,1,4,1,2011,10,2,39,9,1,2,1,5),_H3cVoAAAGwProcessConfig_Type())
h3cVoAAAGwProcessConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAAAGwProcessConfig.setStatus(_A)
class _H3cVoAAAGwCardDigit_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_H3cVoAAAGwCardDigit_Type.__name__=_D
_H3cVoAAAGwCardDigit_Object=MibTableColumn
h3cVoAAAGwCardDigit=_H3cVoAAAGwCardDigit_Object((1,3,6,1,4,1,2011,10,2,39,9,1,2,1,6),_H3cVoAAAGwCardDigit_Type())
h3cVoAAAGwCardDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAAAGwCardDigit.setStatus(_A)
class _H3cVoAAAGwPasswordDigit_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_H3cVoAAAGwPasswordDigit_Type.__name__=_D
_H3cVoAAAGwPasswordDigit_Object=MibTableColumn
h3cVoAAAGwPasswordDigit=_H3cVoAAAGwPasswordDigit_Object((1,3,6,1,4,1,2011,10,2,39,9,1,2,1,7),_H3cVoAAAGwPasswordDigit_Type())
h3cVoAAAGwPasswordDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAAAGwPasswordDigit.setStatus(_A)
class _H3cVoAAAGwRedialTimes_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_H3cVoAAAGwRedialTimes_Type.__name__=_D
_H3cVoAAAGwRedialTimes_Object=MibTableColumn
h3cVoAAAGwRedialTimes=_H3cVoAAAGwRedialTimes_Object((1,3,6,1,4,1,2011,10,2,39,9,1,2,1,8),_H3cVoAAAGwRedialTimes_Type())
h3cVoAAAGwRedialTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAAAGwRedialTimes.setStatus(_A)
_H3cVoAAAGwRowStatus_Type=RowStatus
_H3cVoAAAGwRowStatus_Object=MibTableColumn
h3cVoAAAGwRowStatus=_H3cVoAAAGwRowStatus_Object((1,3,6,1,4,1,2011,10,2,39,9,1,2,1,9),_H3cVoAAAGwRowStatus_Type())
h3cVoAAAGwRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoAAAGwRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'h3cVoiceAAAClient':h3cVoiceAAAClient,'h3cVoAAAClientObjects':h3cVoAAAClientObjects,'h3cVoAAAClientCfgObjects':h3cVoAAAClientCfgObjects,'h3cVoAAAGwAuthenDid':h3cVoAAAGwAuthenDid,'h3cVoAAAGwAuthorDid':h3cVoAAAGwAuthorDid,'h3cVoAAAGwAccountingDid':h3cVoAAAGwAccountingDid,'h3cVoAAAGwAccountMethod':h3cVoAAAGwAccountMethod,'h3cVoAAAGwAccessNumberTable':h3cVoAAAGwAccessNumberTable,'h3cVoAAAGwAccessNumberEntry':h3cVoAAAGwAccessNumberEntry,_H:h3cVoAAAGwAccessNumber,'h3cVoAAAGwAuthentication':h3cVoAAAGwAuthentication,'h3cVoAAAGwAuthorization':h3cVoAAAGwAuthorization,'h3cVoAAAGwAccounting':h3cVoAAAGwAccounting,'h3cVoAAAGwProcessConfig':h3cVoAAAGwProcessConfig,'h3cVoAAAGwCardDigit':h3cVoAAAGwCardDigit,'h3cVoAAAGwPasswordDigit':h3cVoAAAGwPasswordDigit,'h3cVoAAAGwRedialTimes':h3cVoAAAGwRedialTimes,'h3cVoAAAGwRowStatus':h3cVoAAAGwRowStatus})
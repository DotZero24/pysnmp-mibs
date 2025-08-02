_G='dot1xPaePortNumber'
_F='IEEE8021-PAE-MIB'
_E='TruthValue'
_D='Integer32'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
dot1xPaePortNumber,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
h3c8021XExt2=ModuleIdentity((1,3,6,1,4,1,2011,10,2,153))
if mibBuilder.loadTexts:h3c8021XExt2.setRevisions(('2014-03-27 00:00',))
_H3c8021XExt2MibObjects_ObjectIdentity=ObjectIdentity
h3c8021XExt2MibObjects=_H3c8021XExt2MibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,153,1))
_H3c8021XExt2System_ObjectIdentity=ObjectIdentity
h3c8021XExt2System=_H3c8021XExt2System_ObjectIdentity((1,3,6,1,4,1,2011,10,2,153,1,1))
class _H3c8021XExt2AuthQuietPeriod_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,120))
_H3c8021XExt2AuthQuietPeriod_Type.__name__=_C
_H3c8021XExt2AuthQuietPeriod_Object=MibScalar
h3c8021XExt2AuthQuietPeriod=_H3c8021XExt2AuthQuietPeriod_Object((1,3,6,1,4,1,2011,10,2,153,1,1,1),_H3c8021XExt2AuthQuietPeriod_Type())
h3c8021XExt2AuthQuietPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c8021XExt2AuthQuietPeriod.setStatus(_A)
class _H3c8021XExt2AuthTxPeriod_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,120))
_H3c8021XExt2AuthTxPeriod_Type.__name__=_C
_H3c8021XExt2AuthTxPeriod_Object=MibScalar
h3c8021XExt2AuthTxPeriod=_H3c8021XExt2AuthTxPeriod_Object((1,3,6,1,4,1,2011,10,2,153,1,1,2),_H3c8021XExt2AuthTxPeriod_Type())
h3c8021XExt2AuthTxPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c8021XExt2AuthTxPeriod.setStatus(_A)
class _H3c8021XExt2AuthSuppTimeout_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_H3c8021XExt2AuthSuppTimeout_Type.__name__=_C
_H3c8021XExt2AuthSuppTimeout_Object=MibScalar
h3c8021XExt2AuthSuppTimeout=_H3c8021XExt2AuthSuppTimeout_Object((1,3,6,1,4,1,2011,10,2,153,1,1,3),_H3c8021XExt2AuthSuppTimeout_Type())
h3c8021XExt2AuthSuppTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c8021XExt2AuthSuppTimeout.setStatus(_A)
class _H3c8021XExt2AuthServerTimeout_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,300))
_H3c8021XExt2AuthServerTimeout_Type.__name__=_C
_H3c8021XExt2AuthServerTimeout_Object=MibScalar
h3c8021XExt2AuthServerTimeout=_H3c8021XExt2AuthServerTimeout_Object((1,3,6,1,4,1,2011,10,2,153,1,1,4),_H3c8021XExt2AuthServerTimeout_Type())
h3c8021XExt2AuthServerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c8021XExt2AuthServerTimeout.setStatus(_A)
class _H3c8021XExt2AuthMaxReq_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_H3c8021XExt2AuthMaxReq_Type.__name__=_C
_H3c8021XExt2AuthMaxReq_Object=MibScalar
h3c8021XExt2AuthMaxReq=_H3c8021XExt2AuthMaxReq_Object((1,3,6,1,4,1,2011,10,2,153,1,1,5),_H3c8021XExt2AuthMaxReq_Type())
h3c8021XExt2AuthMaxReq.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c8021XExt2AuthMaxReq.setStatus(_A)
class _H3c8021XExt2AuthReAuthPeriod_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,7200))
_H3c8021XExt2AuthReAuthPeriod_Type.__name__=_C
_H3c8021XExt2AuthReAuthPeriod_Object=MibScalar
h3c8021XExt2AuthReAuthPeriod=_H3c8021XExt2AuthReAuthPeriod_Object((1,3,6,1,4,1,2011,10,2,153,1,1,6),_H3c8021XExt2AuthReAuthPeriod_Type())
h3c8021XExt2AuthReAuthPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c8021XExt2AuthReAuthPeriod.setStatus(_A)
class _H3c8021XExt2AuthMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('chap',1),('pap',2),('eap',3)))
_H3c8021XExt2AuthMethod_Type.__name__=_D
_H3c8021XExt2AuthMethod_Object=MibScalar
h3c8021XExt2AuthMethod=_H3c8021XExt2AuthMethod_Object((1,3,6,1,4,1,2011,10,2,153,1,1,7),_H3c8021XExt2AuthMethod_Type())
h3c8021XExt2AuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c8021XExt2AuthMethod.setStatus(_A)
_H3c8021XExt2Authenticator_ObjectIdentity=ObjectIdentity
h3c8021XExt2Authenticator=_H3c8021XExt2Authenticator_ObjectIdentity((1,3,6,1,4,1,2011,10,2,153,1,2))
_H3c8021XExt2AuthConfigExtTable_Object=MibTable
h3c8021XExt2AuthConfigExtTable=_H3c8021XExt2AuthConfigExtTable_Object((1,3,6,1,4,1,2011,10,2,153,1,2,1))
if mibBuilder.loadTexts:h3c8021XExt2AuthConfigExtTable.setStatus(_A)
_H3c8021XExt2AuthConfigExtEntry_Object=MibTableRow
h3c8021XExt2AuthConfigExtEntry=_H3c8021XExt2AuthConfigExtEntry_Object((1,3,6,1,4,1,2011,10,2,153,1,2,1,1))
h3c8021XExt2AuthConfigExtEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3c8021XExt2AuthConfigExtEntry.setStatus(_A)
class _H3c8021XExt2PaePortAuthAdminStatus_Type(TruthValue):defaultValue=2
_H3c8021XExt2PaePortAuthAdminStatus_Type.__name__=_E
_H3c8021XExt2PaePortAuthAdminStatus_Object=MibTableColumn
h3c8021XExt2PaePortAuthAdminStatus=_H3c8021XExt2PaePortAuthAdminStatus_Object((1,3,6,1,4,1,2011,10,2,153,1,2,1,1,1),_H3c8021XExt2PaePortAuthAdminStatus_Type())
h3c8021XExt2PaePortAuthAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c8021XExt2PaePortAuthAdminStatus.setStatus(_A)
class _H3c8021XExt2PaePortControlledType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portbased',1),('macbased',2)))
_H3c8021XExt2PaePortControlledType_Type.__name__=_D
_H3c8021XExt2PaePortControlledType_Object=MibTableColumn
h3c8021XExt2PaePortControlledType=_H3c8021XExt2PaePortControlledType_Object((1,3,6,1,4,1,2011,10,2,153,1,2,1,1,2),_H3c8021XExt2PaePortControlledType_Type())
h3c8021XExt2PaePortControlledType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c8021XExt2PaePortControlledType.setStatus(_A)
class _H3c8021XExt2PaePortMaxUserNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3c8021XExt2PaePortMaxUserNum_Type.__name__=_C
_H3c8021XExt2PaePortMaxUserNum_Object=MibTableColumn
h3c8021XExt2PaePortMaxUserNum=_H3c8021XExt2PaePortMaxUserNum_Object((1,3,6,1,4,1,2011,10,2,153,1,2,1,1,3),_H3c8021XExt2PaePortMaxUserNum_Type())
h3c8021XExt2PaePortMaxUserNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c8021XExt2PaePortMaxUserNum.setStatus(_A)
_H3c8021XExt2PaePortUserNumNow_Type=Unsigned32
_H3c8021XExt2PaePortUserNumNow_Object=MibTableColumn
h3c8021XExt2PaePortUserNumNow=_H3c8021XExt2PaePortUserNumNow_Object((1,3,6,1,4,1,2011,10,2,153,1,2,1,1,4),_H3c8021XExt2PaePortUserNumNow_Type())
h3c8021XExt2PaePortUserNumNow.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3c8021XExt2PaePortUserNumNow.setStatus(_A)
class _H3c8021XExt2PaePortClearStatistics_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noClear',0),('clear',1)))
_H3c8021XExt2PaePortClearStatistics_Type.__name__=_D
_H3c8021XExt2PaePortClearStatistics_Object=MibTableColumn
h3c8021XExt2PaePortClearStatistics=_H3c8021XExt2PaePortClearStatistics_Object((1,3,6,1,4,1,2011,10,2,153,1,2,1,1,5),_H3c8021XExt2PaePortClearStatistics_Type())
h3c8021XExt2PaePortClearStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c8021XExt2PaePortClearStatistics.setStatus(_A)
class _H3c8021XExt2PaePortMcastTrigStatus_Type(TruthValue):defaultValue=1
_H3c8021XExt2PaePortMcastTrigStatus_Type.__name__=_E
_H3c8021XExt2PaePortMcastTrigStatus_Object=MibTableColumn
h3c8021XExt2PaePortMcastTrigStatus=_H3c8021XExt2PaePortMcastTrigStatus_Object((1,3,6,1,4,1,2011,10,2,153,1,2,1,1,6),_H3c8021XExt2PaePortMcastTrigStatus_Type())
h3c8021XExt2PaePortMcastTrigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c8021XExt2PaePortMcastTrigStatus.setStatus(_A)
class _H3c8021XExt2PaePortHandshakeStatus_Type(TruthValue):defaultValue=1
_H3c8021XExt2PaePortHandshakeStatus_Type.__name__=_E
_H3c8021XExt2PaePortHandshakeStatus_Object=MibTableColumn
h3c8021XExt2PaePortHandshakeStatus=_H3c8021XExt2PaePortHandshakeStatus_Object((1,3,6,1,4,1,2011,10,2,153,1,2,1,1,7),_H3c8021XExt2PaePortHandshakeStatus_Type())
h3c8021XExt2PaePortHandshakeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c8021XExt2PaePortHandshakeStatus.setStatus(_A)
mibBuilder.exportSymbols('H3C-8021X-EXT2-MIB',**{'h3c8021XExt2':h3c8021XExt2,'h3c8021XExt2MibObjects':h3c8021XExt2MibObjects,'h3c8021XExt2System':h3c8021XExt2System,'h3c8021XExt2AuthQuietPeriod':h3c8021XExt2AuthQuietPeriod,'h3c8021XExt2AuthTxPeriod':h3c8021XExt2AuthTxPeriod,'h3c8021XExt2AuthSuppTimeout':h3c8021XExt2AuthSuppTimeout,'h3c8021XExt2AuthServerTimeout':h3c8021XExt2AuthServerTimeout,'h3c8021XExt2AuthMaxReq':h3c8021XExt2AuthMaxReq,'h3c8021XExt2AuthReAuthPeriod':h3c8021XExt2AuthReAuthPeriod,'h3c8021XExt2AuthMethod':h3c8021XExt2AuthMethod,'h3c8021XExt2Authenticator':h3c8021XExt2Authenticator,'h3c8021XExt2AuthConfigExtTable':h3c8021XExt2AuthConfigExtTable,'h3c8021XExt2AuthConfigExtEntry':h3c8021XExt2AuthConfigExtEntry,'h3c8021XExt2PaePortAuthAdminStatus':h3c8021XExt2PaePortAuthAdminStatus,'h3c8021XExt2PaePortControlledType':h3c8021XExt2PaePortControlledType,'h3c8021XExt2PaePortMaxUserNum':h3c8021XExt2PaePortMaxUserNum,'h3c8021XExt2PaePortUserNumNow':h3c8021XExt2PaePortUserNumNow,'h3c8021XExt2PaePortClearStatistics':h3c8021XExt2PaePortClearStatistics,'h3c8021XExt2PaePortMcastTrigStatus':h3c8021XExt2PaePortMcastTrigStatus,'h3c8021XExt2PaePortHandshakeStatus':h3c8021XExt2PaePortHandshakeStatus})
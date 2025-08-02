_E='OctetString'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mpSntpMib=ModuleIdentity((1,3,6,1,4,1,5651,3,28))
_SntpGlobal_ObjectIdentity=ObjectIdentity
sntpGlobal=_SntpGlobal_ObjectIdentity((1,3,6,1,4,1,5651,3,28,1))
class _SntpBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_SntpBroadcast_Type.__name__=_C
_SntpBroadcast_Object=MibScalar
sntpBroadcast=_SntpBroadcast_Object((1,3,6,1,4,1,5651,3,28,1,1),_SntpBroadcast_Type())
sntpBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpBroadcast.setStatus(_A)
class _SntpInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_SntpInterval_Type.__name__=_C
_SntpInterval_Object=MibScalar
sntpInterval=_SntpInterval_Object((1,3,6,1,4,1,5651,3,28,1,2),_SntpInterval_Type())
sntpInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpInterval.setStatus(_A)
_SntpSvrName_Type=OctetString
_SntpSvrName_Object=MibScalar
sntpSvrName=_SntpSvrName_Object((1,3,6,1,4,1,5651,3,28,1,3),_SntpSvrName_Type())
sntpSvrName.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpSvrName.setStatus(_A)
class _SntpTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,600))
_SntpTimeout_Type.__name__=_C
_SntpTimeout_Object=MibScalar
sntpTimeout=_SntpTimeout_Object((1,3,6,1,4,1,5651,3,28,1,4),_SntpTimeout_Type())
sntpTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpTimeout.setStatus(_A)
_SntpLeapVerMode_Type=Integer32
_SntpLeapVerMode_Object=MibScalar
sntpLeapVerMode=_SntpLeapVerMode_Object((1,3,6,1,4,1,5651,3,28,1,5),_SntpLeapVerMode_Type())
sntpLeapVerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpLeapVerMode.setStatus(_A)
_SntpStratum_Type=Integer32
_SntpStratum_Object=MibScalar
sntpStratum=_SntpStratum_Object((1,3,6,1,4,1,5651,3,28,1,6),_SntpStratum_Type())
sntpStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpStratum.setStatus(_A)
_SntpPoll_Type=Integer32
_SntpPoll_Object=MibScalar
sntpPoll=_SntpPoll_Object((1,3,6,1,4,1,5651,3,28,1,7),_SntpPoll_Type())
sntpPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpPoll.setStatus(_A)
_SntpPrecision_Type=Integer32
_SntpPrecision_Object=MibScalar
sntpPrecision=_SntpPrecision_Object((1,3,6,1,4,1,5651,3,28,1,8),_SntpPrecision_Type())
sntpPrecision.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpPrecision.setStatus(_A)
_SntpRootDelay_Type=Integer32
_SntpRootDelay_Object=MibScalar
sntpRootDelay=_SntpRootDelay_Object((1,3,6,1,4,1,5651,3,28,1,9),_SntpRootDelay_Type())
sntpRootDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpRootDelay.setStatus(_A)
_SntpRootDispersion_Type=Integer32
_SntpRootDispersion_Object=MibScalar
sntpRootDispersion=_SntpRootDispersion_Object((1,3,6,1,4,1,5651,3,28,1,10),_SntpRootDispersion_Type())
sntpRootDispersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpRootDispersion.setStatus(_A)
_SntpReferenceIdentifier_Type=Integer32
_SntpReferenceIdentifier_Object=MibScalar
sntpReferenceIdentifier=_SntpReferenceIdentifier_Object((1,3,6,1,4,1,5651,3,28,1,11),_SntpReferenceIdentifier_Type())
sntpReferenceIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpReferenceIdentifier.setStatus(_A)
_SntpReferencetimestampsec_Type=Integer32
_SntpReferencetimestampsec_Object=MibScalar
sntpReferencetimestampsec=_SntpReferencetimestampsec_Object((1,3,6,1,4,1,5651,3,28,1,12),_SntpReferencetimestampsec_Type())
sntpReferencetimestampsec.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpReferencetimestampsec.setStatus(_A)
_SntpOriginateTimestampSec_Type=Integer32
_SntpOriginateTimestampSec_Object=MibScalar
sntpOriginateTimestampSec=_SntpOriginateTimestampSec_Object((1,3,6,1,4,1,5651,3,28,1,13),_SntpOriginateTimestampSec_Type())
sntpOriginateTimestampSec.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpOriginateTimestampSec.setStatus(_A)
_SntpReveiveTimestampSec_Type=Integer32
_SntpReveiveTimestampSec_Object=MibScalar
sntpReveiveTimestampSec=_SntpReveiveTimestampSec_Object((1,3,6,1,4,1,5651,3,28,1,14),_SntpReveiveTimestampSec_Type())
sntpReveiveTimestampSec.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpReveiveTimestampSec.setStatus(_A)
_SntpTransmitTimestampSec_Type=Integer32
_SntpTransmitTimestampSec_Object=MibScalar
sntpTransmitTimestampSec=_SntpTransmitTimestampSec_Object((1,3,6,1,4,1,5651,3,28,1,15),_SntpTransmitTimestampSec_Type())
sntpTransmitTimestampSec.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpTransmitTimestampSec.setStatus(_A)
class _SntpSysTimeStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SntpSysTimeStatus_Type.__name__=_E
_SntpSysTimeStatus_Object=MibScalar
sntpSysTimeStatus=_SntpSysTimeStatus_Object((1,3,6,1,4,1,5651,3,28,1,16),_SntpSysTimeStatus_Type())
sntpSysTimeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpSysTimeStatus.setStatus(_A)
_SntpUpdataSysTime_Type=OctetString
_SntpUpdataSysTime_Object=MibScalar
sntpUpdataSysTime=_SntpUpdataSysTime_Object((1,3,6,1,4,1,5651,3,28,1,17),_SntpUpdataSysTime_Type())
sntpUpdataSysTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpUpdataSysTime.setStatus(_A)
_SntpToNowSec_Type=Integer32
_SntpToNowSec_Object=MibScalar
sntpToNowSec=_SntpToNowSec_Object((1,3,6,1,4,1,5651,3,28,1,18),_SntpToNowSec_Type())
sntpToNowSec.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpToNowSec.setStatus(_A)
_SntpRoundtripTime_Type=Integer32
_SntpRoundtripTime_Object=MibScalar
sntpRoundtripTime=_SntpRoundtripTime_Object((1,3,6,1,4,1,5651,3,28,1,19),_SntpRoundtripTime_Type())
sntpRoundtripTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpRoundtripTime.setStatus(_A)
mibBuilder.exportSymbols('MPSNTP-MIB',**{'mpSntpMib':mpSntpMib,'sntpGlobal':sntpGlobal,'sntpBroadcast':sntpBroadcast,'sntpInterval':sntpInterval,'sntpSvrName':sntpSvrName,'sntpTimeout':sntpTimeout,'sntpLeapVerMode':sntpLeapVerMode,'sntpStratum':sntpStratum,'sntpPoll':sntpPoll,'sntpPrecision':sntpPrecision,'sntpRootDelay':sntpRootDelay,'sntpRootDispersion':sntpRootDispersion,'sntpReferenceIdentifier':sntpReferenceIdentifier,'sntpReferencetimestampsec':sntpReferencetimestampsec,'sntpOriginateTimestampSec':sntpOriginateTimestampSec,'sntpReveiveTimestampSec':sntpReveiveTimestampSec,'sntpTransmitTimestampSec':sntpTransmitTimestampSec,'sntpSysTimeStatus':sntpSysTimeStatus,'sntpUpdataSysTime':sntpUpdataSysTime,'sntpToNowSec':sntpToNowSec,'sntpRoundtripTime':sntpRoundtripTime})
_F='bmpActionDisable'
_E='bmpActionEnable'
_D='OctetString'
_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dellNetMgmt,=mibBuilder.importSymbols('DELL-NETWORKING-SMI','dellNetMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dellNetBmpMib=ModuleIdentity((1,3,6,1,4,1,6027,3,23))
if mibBuilder.loadTexts:dellNetBmpMib.setRevisions(('2014-07-21 12:00','2011-12-07 12:48'))
_DellNetBmp_ObjectIdentity=ObjectIdentity
dellNetBmp=_DellNetBmp_ObjectIdentity((1,3,6,1,4,1,6027,3,23,1))
class _BmpReloadType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normalReload',1),('bmpReload',2)))
_BmpReloadType_Type.__name__=_C
_BmpReloadType_Object=MibScalar
bmpReloadType=_BmpReloadType_Object((1,3,6,1,4,1,6027,3,23,1,1),_BmpReloadType_Type())
bmpReloadType.setMaxAccess(_A)
if mibBuilder.loadTexts:bmpReloadType.setStatus(_B)
class _BmpAutoSave_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BmpAutoSave_Type.__name__=_C
_BmpAutoSave_Object=MibScalar
bmpAutoSave=_BmpAutoSave_Object((1,3,6,1,4,1,6027,3,23,1,2),_BmpAutoSave_Type())
bmpAutoSave.setMaxAccess(_A)
if mibBuilder.loadTexts:bmpAutoSave.setStatus(_B)
class _BmpConfigDownload_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BmpConfigDownload_Type.__name__=_C
_BmpConfigDownload_Object=MibScalar
bmpConfigDownload=_BmpConfigDownload_Object((1,3,6,1,4,1,6027,3,23,1,3),_BmpConfigDownload_Type())
bmpConfigDownload.setMaxAccess(_A)
if mibBuilder.loadTexts:bmpConfigDownload.setStatus(_B)
class _BmpDhcpTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_BmpDhcpTimeout_Type.__name__=_C
_BmpDhcpTimeout_Object=MibScalar
bmpDhcpTimeout=_BmpDhcpTimeout_Object((1,3,6,1,4,1,6027,3,23,1,4),_BmpDhcpTimeout_Type())
bmpDhcpTimeout.setMaxAccess(_A)
if mibBuilder.loadTexts:bmpDhcpTimeout.setStatus(_B)
class _BmpRetryCount_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_BmpRetryCount_Type.__name__=_C
_BmpRetryCount_Object=MibScalar
bmpRetryCount=_BmpRetryCount_Object((1,3,6,1,4,1,6027,3,23,1,5),_BmpRetryCount_Type())
bmpRetryCount.setMaxAccess(_A)
if mibBuilder.loadTexts:bmpRetryCount.setStatus(_B)
class _BmpUserDefinedString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BmpUserDefinedString_Type.__name__=_D
_BmpUserDefinedString_Object=MibScalar
bmpUserDefinedString=_BmpUserDefinedString_Object((1,3,6,1,4,1,6027,3,23,1,6),_BmpUserDefinedString_Type())
bmpUserDefinedString.setMaxAccess(_A)
if mibBuilder.loadTexts:bmpUserDefinedString.setStatus(_B)
class _BmpRelay_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BmpRelay_Type.__name__=_C
_BmpRelay_Object=MibScalar
bmpRelay=_BmpRelay_Object((1,3,6,1,4,1,6027,3,23,1,7),_BmpRelay_Type())
bmpRelay.setMaxAccess(_A)
if mibBuilder.loadTexts:bmpRelay.setStatus(_B)
class _BmpRelayRemoteId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BmpRelayRemoteId_Type.__name__=_D
_BmpRelayRemoteId_Object=MibScalar
bmpRelayRemoteId=_BmpRelayRemoteId_Object((1,3,6,1,4,1,6027,3,23,1,8),_BmpRelayRemoteId_Type())
bmpRelayRemoteId.setMaxAccess(_A)
if mibBuilder.loadTexts:bmpRelayRemoteId.setStatus(_B)
mibBuilder.exportSymbols('DELL-NETWORKING-BMP-MIB',**{'dellNetBmpMib':dellNetBmpMib,'dellNetBmp':dellNetBmp,'bmpReloadType':bmpReloadType,'bmpAutoSave':bmpAutoSave,'bmpConfigDownload':bmpConfigDownload,'bmpDhcpTimeout':bmpDhcpTimeout,'bmpRetryCount':bmpRetryCount,'bmpUserDefinedString':bmpUserDefinedString,'bmpRelay':bmpRelay,'bmpRelayRemoteId':bmpRelayRemoteId})
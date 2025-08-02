if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
dlinkPrimeSslMIB=ModuleIdentity((1,3,6,1,4,1,171,15,16))
if mibBuilder.loadTexts:dlinkPrimeSslMIB.setRevisions(('2014-04-26 00:00',))
_DpSslNotifications_ObjectIdentity=ObjectIdentity
dpSslNotifications=_DpSslNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,16,0))
_DpSslObjects_ObjectIdentity=ObjectIdentity
dpSslObjects=_DpSslObjects_ObjectIdentity((1,3,6,1,4,1,171,15,16,1))
_DpSslConfiguration_ObjectIdentity=ObjectIdentity
dpSslConfiguration=_DpSslConfiguration_ObjectIdentity((1,3,6,1,4,1,171,15,16,1,1))
_DpSslServiceEnabled_Type=TruthValue
_DpSslServiceEnabled_Object=MibScalar
dpSslServiceEnabled=_DpSslServiceEnabled_Object((1,3,6,1,4,1,171,15,16,1,1,1),_DpSslServiceEnabled_Type())
dpSslServiceEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:dpSslServiceEnabled.setStatus('current')
_DpSslConformance_ObjectIdentity=ObjectIdentity
dpSslConformance=_DpSslConformance_ObjectIdentity((1,3,6,1,4,1,171,15,16,2))
mibBuilder.exportSymbols('DLINKPRIME-SSL-MIB',**{'dlinkPrimeSslMIB':dlinkPrimeSslMIB,'dpSslNotifications':dpSslNotifications,'dpSslObjects':dpSslObjects,'dpSslConfiguration':dpSslConfiguration,'dpSslServiceEnabled':dpSslServiceEnabled,'dpSslConformance':dpSslConformance})
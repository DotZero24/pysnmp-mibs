_F='enable'
_E='disable'
_D='DisplayString'
_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arrisProdIdCM,=mibBuilder.importSymbols('ARRIS-MIB','arrisProdIdCM')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'PhysAddress','TextualConvention','TimeStamp','TruthValue')
arrisMtaDoc30Mib=ModuleIdentity((1,3,6,1,4,1,4115,1,3,5))
if mibBuilder.loadTexts:arrisMtaDoc30Mib.setRevisions(('1910-10-20 00:00',))
_ArrisMtaDoc30MibObjects_ObjectIdentity=ObjectIdentity
arrisMtaDoc30MibObjects=_ArrisMtaDoc30MibObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,3,5,1))
_ArrisMtaDoc30Base_ObjectIdentity=ObjectIdentity
arrisMtaDoc30Base=_ArrisMtaDoc30Base_ObjectIdentity((1,3,6,1,4,1,4115,1,3,5,1,1))
_ArrisMtaDoc30Setup_ObjectIdentity=ObjectIdentity
arrisMtaDoc30Setup=_ArrisMtaDoc30Setup_ObjectIdentity((1,3,6,1,4,1,4115,1,3,5,1,2))
class _ArrisMtaDoc30EmergencyNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_ArrisMtaDoc30EmergencyNumber_Type.__name__=_D
_ArrisMtaDoc30EmergencyNumber_Object=MibScalar
arrisMtaDoc30EmergencyNumber=_ArrisMtaDoc30EmergencyNumber_Object((1,3,6,1,4,1,4115,1,3,5,1,2,1),_ArrisMtaDoc30EmergencyNumber_Type())
arrisMtaDoc30EmergencyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisMtaDoc30EmergencyNumber.setStatus(_C)
class _ArrisMtaDoc30RootCertType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('testRoot',1),('realRoot',2)))
_ArrisMtaDoc30RootCertType_Type.__name__=_A
_ArrisMtaDoc30RootCertType_Object=MibScalar
arrisMtaDoc30RootCertType=_ArrisMtaDoc30RootCertType_Object((1,3,6,1,4,1,4115,1,3,5,1,2,2),_ArrisMtaDoc30RootCertType_Type())
arrisMtaDoc30RootCertType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisMtaDoc30RootCertType.setStatus(_C)
class _ArrisMtaDoc30AdjustCallpFeatureSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ArrisMtaDoc30AdjustCallpFeatureSwitch_Type.__name__=_A
_ArrisMtaDoc30AdjustCallpFeatureSwitch_Object=MibScalar
arrisMtaDoc30AdjustCallpFeatureSwitch=_ArrisMtaDoc30AdjustCallpFeatureSwitch_Object((1,3,6,1,4,1,4115,1,3,5,1,2,3),_ArrisMtaDoc30AdjustCallpFeatureSwitch_Type())
arrisMtaDoc30AdjustCallpFeatureSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisMtaDoc30AdjustCallpFeatureSwitch.setStatus(_C)
class _ArrisMtaDoc30InvalidateTickets_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ArrisMtaDoc30InvalidateTickets_Type.__name__=_A
_ArrisMtaDoc30InvalidateTickets_Object=MibScalar
arrisMtaDoc30InvalidateTickets=_ArrisMtaDoc30InvalidateTickets_Object((1,3,6,1,4,1,4115,1,3,5,1,2,4),_ArrisMtaDoc30InvalidateTickets_Type())
arrisMtaDoc30InvalidateTickets.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisMtaDoc30InvalidateTickets.setStatus(_C)
mibBuilder.exportSymbols('ARRIS-MTA-DOC30-DEVICE-MIB',**{'arrisMtaDoc30Mib':arrisMtaDoc30Mib,'arrisMtaDoc30MibObjects':arrisMtaDoc30MibObjects,'arrisMtaDoc30Base':arrisMtaDoc30Base,'arrisMtaDoc30Setup':arrisMtaDoc30Setup,'arrisMtaDoc30EmergencyNumber':arrisMtaDoc30EmergencyNumber,'arrisMtaDoc30RootCertType':arrisMtaDoc30RootCertType,'arrisMtaDoc30AdjustCallpFeatureSwitch':arrisMtaDoc30AdjustCallpFeatureSwitch,'arrisMtaDoc30InvalidateTickets':arrisMtaDoc30InvalidateTickets})
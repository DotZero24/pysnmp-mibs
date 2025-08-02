_I='me1200UpnpConfigGlobalsInfoGroup'
_H='me1200UpnpConfigGlobalsAdvertisingDuration'
_G='me1200UpnpConfigGlobalsTtl'
_F='me1200UpnpConfigGlobalsMode'
_E='Integer32'
_D='ME1200Unsigned8'
_C='read-write'
_B='ME1200-UPNP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
me1200SwitchMgmt,=mibBuilder.importSymbols('CISCOME1200-MIB','me1200SwitchMgmt')
ME1200Unsigned8,=mibBuilder.importSymbols('ME1200-TC',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
me1200UpnpMib=ModuleIdentity((1,3,6,1,4,1,9,9,815,1,52))
if mibBuilder.loadTexts:me1200UpnpMib.setRevisions(('2014-04-14 00:00',))
_Me1200UpnpMibObjects_ObjectIdentity=ObjectIdentity
me1200UpnpMibObjects=_Me1200UpnpMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,52,1))
_Me1200UpnpConfig_ObjectIdentity=ObjectIdentity
me1200UpnpConfig=_Me1200UpnpConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,52,1,2))
_Me1200UpnpConfigGlobals_ObjectIdentity=ObjectIdentity
me1200UpnpConfigGlobals=_Me1200UpnpConfigGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,52,1,2,1))
_Me1200UpnpConfigGlobalsMode_Type=TruthValue
_Me1200UpnpConfigGlobalsMode_Object=MibScalar
me1200UpnpConfigGlobalsMode=_Me1200UpnpConfigGlobalsMode_Object((1,3,6,1,4,1,9,9,815,1,52,1,2,1,1),_Me1200UpnpConfigGlobalsMode_Type())
me1200UpnpConfigGlobalsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UpnpConfigGlobalsMode.setStatus(_A)
class _Me1200UpnpConfigGlobalsTtl_Type(ME1200Unsigned8):subtypeSpec=ME1200Unsigned8.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Me1200UpnpConfigGlobalsTtl_Type.__name__=_D
_Me1200UpnpConfigGlobalsTtl_Object=MibScalar
me1200UpnpConfigGlobalsTtl=_Me1200UpnpConfigGlobalsTtl_Object((1,3,6,1,4,1,9,9,815,1,52,1,2,1,2),_Me1200UpnpConfigGlobalsTtl_Type())
me1200UpnpConfigGlobalsTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UpnpConfigGlobalsTtl.setStatus(_A)
class _Me1200UpnpConfigGlobalsAdvertisingDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,86400))
_Me1200UpnpConfigGlobalsAdvertisingDuration_Type.__name__=_E
_Me1200UpnpConfigGlobalsAdvertisingDuration_Object=MibScalar
me1200UpnpConfigGlobalsAdvertisingDuration=_Me1200UpnpConfigGlobalsAdvertisingDuration_Object((1,3,6,1,4,1,9,9,815,1,52,1,2,1,3),_Me1200UpnpConfigGlobalsAdvertisingDuration_Type())
me1200UpnpConfigGlobalsAdvertisingDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UpnpConfigGlobalsAdvertisingDuration.setStatus(_A)
_Me1200UpnpMibConformance_ObjectIdentity=ObjectIdentity
me1200UpnpMibConformance=_Me1200UpnpMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,52,2))
_Me1200UpnpMibCompliances_ObjectIdentity=ObjectIdentity
me1200UpnpMibCompliances=_Me1200UpnpMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,52,2,1))
_Me1200UpnpMibGroups_ObjectIdentity=ObjectIdentity
me1200UpnpMibGroups=_Me1200UpnpMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,52,2,2))
me1200UpnpConfigGlobalsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,52,2,2,1))
me1200UpnpConfigGlobalsInfoGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:me1200UpnpConfigGlobalsInfoGroup.setStatus(_A)
me1200UpnpMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,815,1,52,2,1,1))
me1200UpnpMibCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:me1200UpnpMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'me1200UpnpMib':me1200UpnpMib,'me1200UpnpMibObjects':me1200UpnpMibObjects,'me1200UpnpConfig':me1200UpnpConfig,'me1200UpnpConfigGlobals':me1200UpnpConfigGlobals,_F:me1200UpnpConfigGlobalsMode,_G:me1200UpnpConfigGlobalsTtl,_H:me1200UpnpConfigGlobalsAdvertisingDuration,'me1200UpnpMibConformance':me1200UpnpMibConformance,'me1200UpnpMibCompliances':me1200UpnpMibCompliances,'me1200UpnpMibCompliance':me1200UpnpMibCompliance,'me1200UpnpMibGroups':me1200UpnpMibGroups,_I:me1200UpnpConfigGlobalsInfoGroup})
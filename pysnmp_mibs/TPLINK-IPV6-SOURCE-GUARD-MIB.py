_F='read-only'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkIpv6SourceGuardMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,94))
if mibBuilder.loadTexts:tplinkIpv6SourceGuardMIB.setRevisions(('2012-12-13 09:30',))
_TplinkIpv6SourceGuardMIBObjects_ObjectIdentity=ObjectIdentity
tplinkIpv6SourceGuardMIBObjects=_TplinkIpv6SourceGuardMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,94,1))
_TpIpv6SourceGuardConfig_ObjectIdentity=ObjectIdentity
tpIpv6SourceGuardConfig=_TpIpv6SourceGuardConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,94,1,1))
_TpIpv6SourceGuardConfigTable_Object=MibTable
tpIpv6SourceGuardConfigTable=_TpIpv6SourceGuardConfigTable_Object((1,3,6,1,4,1,11863,6,94,1,1,1))
if mibBuilder.loadTexts:tpIpv6SourceGuardConfigTable.setStatus(_A)
_TpIpv6SourceGuardConfigEntry_Object=MibTableRow
tpIpv6SourceGuardConfigEntry=_TpIpv6SourceGuardConfigEntry_Object((1,3,6,1,4,1,11863,6,94,1,1,1,1))
tpIpv6SourceGuardConfigEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:tpIpv6SourceGuardConfigEntry.setStatus(_A)
class _TpIpv6SourceGuardConfigPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_TpIpv6SourceGuardConfigPort_Type.__name__=_B
_TpIpv6SourceGuardConfigPort_Object=MibTableColumn
tpIpv6SourceGuardConfigPort=_TpIpv6SourceGuardConfigPort_Object((1,3,6,1,4,1,11863,6,94,1,1,1,1,1),_TpIpv6SourceGuardConfigPort_Type())
tpIpv6SourceGuardConfigPort.setMaxAccess(_F)
if mibBuilder.loadTexts:tpIpv6SourceGuardConfigPort.setStatus(_A)
class _TpIpv6SourceGuardConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,0,2)));namedValues=NamedValues(*(('disable',0),('sipv6',0),('sipv6-mac',2)))
_TpIpv6SourceGuardConfigType_Type.__name__=_E
_TpIpv6SourceGuardConfigType_Object=MibTableColumn
tpIpv6SourceGuardConfigType=_TpIpv6SourceGuardConfigType_Object((1,3,6,1,4,1,11863,6,94,1,1,1,1,2),_TpIpv6SourceGuardConfigType_Type())
tpIpv6SourceGuardConfigType.setMaxAccess('read-write')
if mibBuilder.loadTexts:tpIpv6SourceGuardConfigType.setStatus(_A)
class _TpIpv6SourceGuardConfigPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_TpIpv6SourceGuardConfigPortLag_Type.__name__=_B
_TpIpv6SourceGuardConfigPortLag_Object=MibTableColumn
tpIpv6SourceGuardConfigPortLag=_TpIpv6SourceGuardConfigPortLag_Object((1,3,6,1,4,1,11863,6,94,1,1,1,1,3),_TpIpv6SourceGuardConfigPortLag_Type())
tpIpv6SourceGuardConfigPortLag.setMaxAccess(_F)
if mibBuilder.loadTexts:tpIpv6SourceGuardConfigPortLag.setStatus(_A)
_TplinkIpv6SourceGuardNotifications_ObjectIdentity=ObjectIdentity
tplinkIpv6SourceGuardNotifications=_TplinkIpv6SourceGuardNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,94,2))
mibBuilder.exportSymbols('TPLINK-IPV6-SOURCE-GUARD-MIB',**{'tplinkIpv6SourceGuardMIB':tplinkIpv6SourceGuardMIB,'tplinkIpv6SourceGuardMIBObjects':tplinkIpv6SourceGuardMIBObjects,'tpIpv6SourceGuardConfig':tpIpv6SourceGuardConfig,'tpIpv6SourceGuardConfigTable':tpIpv6SourceGuardConfigTable,'tpIpv6SourceGuardConfigEntry':tpIpv6SourceGuardConfigEntry,'tpIpv6SourceGuardConfigPort':tpIpv6SourceGuardConfigPort,'tpIpv6SourceGuardConfigType':tpIpv6SourceGuardConfigType,'tpIpv6SourceGuardConfigPortLag':tpIpv6SourceGuardConfigPortLag,'tplinkIpv6SourceGuardNotifications':tplinkIpv6SourceGuardNotifications})
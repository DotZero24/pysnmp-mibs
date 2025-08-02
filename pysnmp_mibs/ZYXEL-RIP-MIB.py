_F='zyRouteDomainIpMaskBits'
_E='zyRouteDomainIpAddress'
_D='ZYXEL-IP-FORWARD-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyRouteDomainIpAddress,zyRouteDomainIpMaskBits=mibBuilder.importSymbols(_D,_E,_F)
zyxelRip=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,74))
_ZyxelRipSetup_ObjectIdentity=ObjectIdentity
zyxelRipSetup=_ZyxelRipSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,74,1))
_ZyRipState_Type=EnabledStatus
_ZyRipState_Object=MibScalar
zyRipState=_ZyRipState_Object((1,3,6,1,4,1,890,1,15,3,74,1,1),_ZyRipState_Type())
zyRipState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRipState.setStatus(_A)
_ZyRipDistance_Type=Integer32
_ZyRipDistance_Object=MibScalar
zyRipDistance=_ZyRipDistance_Object((1,3,6,1,4,1,890,1,15,3,74,1,2),_ZyRipDistance_Type())
zyRipDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRipDistance.setStatus(_A)
_ZyxelRipRouteDomainTable_Object=MibTable
zyxelRipRouteDomainTable=_ZyxelRipRouteDomainTable_Object((1,3,6,1,4,1,890,1,15,3,74,1,3))
if mibBuilder.loadTexts:zyxelRipRouteDomainTable.setStatus(_A)
_ZyxelRipRouteDomainEntry_Object=MibTableRow
zyxelRipRouteDomainEntry=_ZyxelRipRouteDomainEntry_Object((1,3,6,1,4,1,890,1,15,3,74,1,3,1))
zyxelRipRouteDomainEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:zyxelRipRouteDomainEntry.setStatus(_A)
class _ZyRipRouteDomainDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('outgoing',1),('incoming',2),('both',3)))
_ZyRipRouteDomainDirection_Type.__name__=_C
_ZyRipRouteDomainDirection_Object=MibTableColumn
zyRipRouteDomainDirection=_ZyRipRouteDomainDirection_Object((1,3,6,1,4,1,890,1,15,3,74,1,3,1,1),_ZyRipRouteDomainDirection_Type())
zyRipRouteDomainDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRipRouteDomainDirection.setStatus(_A)
class _ZyRipRouteDomainVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('v1',0),('v2b',1),('v2m',2)))
_ZyRipRouteDomainVersion_Type.__name__=_C
_ZyRipRouteDomainVersion_Object=MibTableColumn
zyRipRouteDomainVersion=_ZyRipRouteDomainVersion_Object((1,3,6,1,4,1,890,1,15,3,74,1,3,1,2),_ZyRipRouteDomainVersion_Type())
zyRipRouteDomainVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRipRouteDomainVersion.setStatus(_A)
_ZyxelRipNotifications_ObjectIdentity=ObjectIdentity
zyxelRipNotifications=_ZyxelRipNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,74,2))
zyRipExceedMaxDynamicRoute=NotificationType((1,3,6,1,4,1,890,1,15,3,74,2,1))
if mibBuilder.loadTexts:zyRipExceedMaxDynamicRoute.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-RIP-MIB',**{'zyxelRip':zyxelRip,'zyxelRipSetup':zyxelRipSetup,'zyRipState':zyRipState,'zyRipDistance':zyRipDistance,'zyxelRipRouteDomainTable':zyxelRipRouteDomainTable,'zyxelRipRouteDomainEntry':zyxelRipRouteDomainEntry,'zyRipRouteDomainDirection':zyRipRouteDomainDirection,'zyRipRouteDomainVersion':zyRipRouteDomainVersion,'zyxelRipNotifications':zyxelRipNotifications,'zyRipExceedMaxDynamicRoute':zyRipExceedMaxDynamicRoute})
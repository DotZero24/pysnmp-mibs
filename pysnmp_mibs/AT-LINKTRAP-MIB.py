_F='current'
_E='ifOperStatus'
_D='ifIndex'
_C='ifDescr'
_B='ifAdminStatus'
_A='IF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sysinfo,=mibBuilder.importSymbols('AT-SMI-MIB','sysinfo')
ifAdminStatus,ifDescr,ifIndex,ifOperStatus=mibBuilder.importSymbols(_A,_B,_C,_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
atLinkTrap=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3,25))
if mibBuilder.loadTexts:atLinkTrap.setRevisions(('2014-04-04 00:00',))
atLinkDown=NotificationType((1,3,6,1,4,1,207,8,4,4,3,25,1))
atLinkDown.setObjects(*((_A,_D),(_A,_B),(_A,_E),(_A,_C)))
if mibBuilder.loadTexts:atLinkDown.setStatus(_F)
atLinkUp=NotificationType((1,3,6,1,4,1,207,8,4,4,3,25,2))
atLinkUp.setObjects(*((_A,_D),(_A,_B),(_A,_E),(_A,_C)))
if mibBuilder.loadTexts:atLinkUp.setStatus(_F)
mibBuilder.exportSymbols('AT-LINKTRAP-MIB',**{'atLinkTrap':atLinkTrap,'atLinkDown':atLinkDown,'atLinkUp':atLinkUp})
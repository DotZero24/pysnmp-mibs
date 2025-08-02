if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
panasas=ModuleIdentity((1,3,6,1,4,1,10159))
if mibBuilder.loadTexts:panasas.setRevisions(('2011-04-07 00:00',))
_PanProducts_ObjectIdentity=ObjectIdentity
panProducts=_PanProducts_ObjectIdentity((1,3,6,1,4,1,10159,1))
_PanNotifications_ObjectIdentity=ObjectIdentity
panNotifications=_PanNotifications_ObjectIdentity((1,3,6,1,4,1,10159,1,1))
_PanHw_ObjectIdentity=ObjectIdentity
panHw=_PanHw_ObjectIdentity((1,3,6,1,4,1,10159,1,2))
_PanFs_ObjectIdentity=ObjectIdentity
panFs=_PanFs_ObjectIdentity((1,3,6,1,4,1,10159,1,3))
mibBuilder.exportSymbols('PANASAS-ROOT-MIB',**{'panasas':panasas,'panProducts':panProducts,'panNotifications':panNotifications,'panHw':panHw,'panFs':panFs})
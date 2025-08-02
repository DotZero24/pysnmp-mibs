_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
papouchProjekt=ModuleIdentity((1,3,6,1,4,1,18248))
if mibBuilder.loadTexts:papouchProjekt.setRevisions(('2006-04-07 00:00',))
_Tme_ObjectIdentity=ObjectIdentity
tme=_Tme_ObjectIdentity((1,3,6,1,4,1,18248,1))
if mibBuilder.loadTexts:tme.setStatus(_A)
_Quido_ObjectIdentity=ObjectIdentity
quido=_Quido_ObjectIdentity((1,3,6,1,4,1,18248,2))
if mibBuilder.loadTexts:quido.setStatus(_A)
_Eccitace_ObjectIdentity=ObjectIdentity
eccitace=_Eccitace_ObjectIdentity((1,3,6,1,4,1,18248,3))
if mibBuilder.loadTexts:eccitace.setStatus(_A)
_E_monitor_ObjectIdentity=ObjectIdentity
e_monitor=_E_monitor_ObjectIdentity((1,3,6,1,4,1,18248,4))
if mibBuilder.loadTexts:e_monitor.setStatus(_A)
mibBuilder.exportSymbols('Papouch-SMI',**{'papouchProjekt':papouchProjekt,'tme':tme,'quido':quido,'eccitace':eccitace,'e_monitor':e_monitor})
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
broadcom=ModuleIdentity((1,3,6,1,4,1,789,4413))
if mibBuilder.loadTexts:broadcom.setRevisions(('2007-05-23 00:00','2003-11-21 00:00','2003-02-06 12:00'))
class AgentPortMask(TextualConvention,OctetString):status='current'
_Netapp_ObjectIdentity=ObjectIdentity
netapp=_Netapp_ObjectIdentity((1,3,6,1,4,1,789))
_BroadcomProducts_ObjectIdentity=ObjectIdentity
broadcomProducts=_BroadcomProducts_ObjectIdentity((1,3,6,1,4,1,789,4413,1))
_FastPath_ObjectIdentity=ObjectIdentity
fastPath=_FastPath_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1))
mibBuilder.exportSymbols('NETAPP-REF-MIB',**{'AgentPortMask':AgentPortMask,'netapp':netapp,'broadcom':broadcom,'broadcomProducts':broadcomProducts,'fastPath':fastPath})
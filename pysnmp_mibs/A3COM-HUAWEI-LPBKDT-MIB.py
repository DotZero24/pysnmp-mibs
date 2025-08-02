_F='h3cLpbkdtVlanID'
_E='A3COM-HUAWEI-LPBKDT-MIB'
_D='current'
_C='ifIndex'
_B='ifDescr'
_A='IF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_A,_B,_C)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cLpbkdt=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,95))
if mibBuilder.loadTexts:h3cLpbkdt.setRevisions(('2009-03-30 17:41','2008-09-27 15:04'))
_H3cLpbkdtNotifications_ObjectIdentity=ObjectIdentity
h3cLpbkdtNotifications=_H3cLpbkdtNotifications_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,95,1))
_H3cLpbkdtTrapPrefix_ObjectIdentity=ObjectIdentity
h3cLpbkdtTrapPrefix=_H3cLpbkdtTrapPrefix_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,95,1,0))
_H3cLpbkdtObjects_ObjectIdentity=ObjectIdentity
h3cLpbkdtObjects=_H3cLpbkdtObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,95,2))
_H3cLpbkdtVlanID_Type=VlanId
_H3cLpbkdtVlanID_Object=MibScalar
h3cLpbkdtVlanID=_H3cLpbkdtVlanID_Object((1,3,6,1,4,1,43,45,1,10,2,95,2,1),_H3cLpbkdtVlanID_Type())
h3cLpbkdtVlanID.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cLpbkdtVlanID.setStatus(_D)
h3cLpbkdtTrapLoopbacked=NotificationType((1,3,6,1,4,1,43,45,1,10,2,95,1,0,1))
h3cLpbkdtTrapLoopbacked.setObjects(*((_A,_C),(_A,_B)))
if mibBuilder.loadTexts:h3cLpbkdtTrapLoopbacked.setStatus(_D)
h3cLpbkdtTrapRecovered=NotificationType((1,3,6,1,4,1,43,45,1,10,2,95,1,0,2))
h3cLpbkdtTrapRecovered.setObjects(*((_A,_C),(_A,_B)))
if mibBuilder.loadTexts:h3cLpbkdtTrapRecovered.setStatus(_D)
h3cLpbkdtTrapPerVlanLoopbacked=NotificationType((1,3,6,1,4,1,43,45,1,10,2,95,1,0,3))
h3cLpbkdtTrapPerVlanLoopbacked.setObjects(*((_A,_C),(_A,_B),(_E,_F)))
if mibBuilder.loadTexts:h3cLpbkdtTrapPerVlanLoopbacked.setStatus(_D)
h3cLpbkdtTrapPerVlanRecovered=NotificationType((1,3,6,1,4,1,43,45,1,10,2,95,1,0,4))
h3cLpbkdtTrapPerVlanRecovered.setObjects(*((_A,_C),(_A,_B),(_E,_F)))
if mibBuilder.loadTexts:h3cLpbkdtTrapPerVlanRecovered.setStatus(_D)
mibBuilder.exportSymbols(_E,**{'h3cLpbkdt':h3cLpbkdt,'h3cLpbkdtNotifications':h3cLpbkdtNotifications,'h3cLpbkdtTrapPrefix':h3cLpbkdtTrapPrefix,'h3cLpbkdtTrapLoopbacked':h3cLpbkdtTrapLoopbacked,'h3cLpbkdtTrapRecovered':h3cLpbkdtTrapRecovered,'h3cLpbkdtTrapPerVlanLoopbacked':h3cLpbkdtTrapPerVlanLoopbacked,'h3cLpbkdtTrapPerVlanRecovered':h3cLpbkdtTrapPerVlanRecovered,'h3cLpbkdtObjects':h3cLpbkdtObjects,_F:h3cLpbkdtVlanID})
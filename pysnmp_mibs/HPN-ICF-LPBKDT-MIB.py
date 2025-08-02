_F='hpnicfLpbkdtVlanID'
_E='HPN-ICF-LPBKDT-MIB'
_D='current'
_C='ifIndex'
_B='ifDescr'
_A='IF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_A,_B,_C)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfLpbkdt=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,95))
if mibBuilder.loadTexts:hpnicfLpbkdt.setRevisions(('2009-03-30 17:41','2008-09-27 15:04'))
_HpnicfLpbkdtNotifications_ObjectIdentity=ObjectIdentity
hpnicfLpbkdtNotifications=_HpnicfLpbkdtNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,95,1))
_HpnicfLpbkdtTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfLpbkdtTrapPrefix=_HpnicfLpbkdtTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,95,1,0))
_HpnicfLpbkdtObjects_ObjectIdentity=ObjectIdentity
hpnicfLpbkdtObjects=_HpnicfLpbkdtObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,95,2))
_HpnicfLpbkdtVlanID_Type=VlanId
_HpnicfLpbkdtVlanID_Object=MibScalar
hpnicfLpbkdtVlanID=_HpnicfLpbkdtVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,95,2,1),_HpnicfLpbkdtVlanID_Type())
hpnicfLpbkdtVlanID.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpnicfLpbkdtVlanID.setStatus(_D)
hpnicfLpbkdtTrapLoopbacked=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,95,1,0,1))
hpnicfLpbkdtTrapLoopbacked.setObjects(*((_A,_C),(_A,_B)))
if mibBuilder.loadTexts:hpnicfLpbkdtTrapLoopbacked.setStatus(_D)
hpnicfLpbkdtTrapRecovered=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,95,1,0,2))
hpnicfLpbkdtTrapRecovered.setObjects(*((_A,_C),(_A,_B)))
if mibBuilder.loadTexts:hpnicfLpbkdtTrapRecovered.setStatus(_D)
hpnicfLpbkdtTrapPerVlanLoopbacked=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,95,1,0,3))
hpnicfLpbkdtTrapPerVlanLoopbacked.setObjects(*((_A,_C),(_A,_B),(_E,_F)))
if mibBuilder.loadTexts:hpnicfLpbkdtTrapPerVlanLoopbacked.setStatus(_D)
hpnicfLpbkdtTrapPerVlanRecovered=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,95,1,0,4))
hpnicfLpbkdtTrapPerVlanRecovered.setObjects(*((_A,_C),(_A,_B),(_E,_F)))
if mibBuilder.loadTexts:hpnicfLpbkdtTrapPerVlanRecovered.setStatus(_D)
mibBuilder.exportSymbols(_E,**{'hpnicfLpbkdt':hpnicfLpbkdt,'hpnicfLpbkdtNotifications':hpnicfLpbkdtNotifications,'hpnicfLpbkdtTrapPrefix':hpnicfLpbkdtTrapPrefix,'hpnicfLpbkdtTrapLoopbacked':hpnicfLpbkdtTrapLoopbacked,'hpnicfLpbkdtTrapRecovered':hpnicfLpbkdtTrapRecovered,'hpnicfLpbkdtTrapPerVlanLoopbacked':hpnicfLpbkdtTrapPerVlanLoopbacked,'hpnicfLpbkdtTrapPerVlanRecovered':hpnicfLpbkdtTrapPerVlanRecovered,'hpnicfLpbkdtObjects':hpnicfLpbkdtObjects,_F:hpnicfLpbkdtVlanID})
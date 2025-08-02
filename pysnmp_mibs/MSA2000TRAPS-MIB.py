_E='NotificationType'
_D='connUnitEventType'
_C='connUnitEventId'
_B='connUnitEventDescr'
_A='FCMGMT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
connUnitEventDescr,connUnitEventId,connUnitEventType=mibBuilder.importSymbols(_A,_B,_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_HpMSA_ObjectIdentity=ObjectIdentity
hpMSA=_HpMSA_ObjectIdentity((1,3,6,1,4,1,11,2,51))
_MibName_Type=Integer32
_MibName_Object=MibScalar
mibName=_MibName_Object((1,3,6,1,4,1,11,2,51,1),_MibName_Type())
mibName.setMaxAccess('read-only')
if mibBuilder.loadTexts:mibName.setStatus('mandatory')
msaEventInfoTrap=NotificationType((1,3,6,1,4,1,11,2,51,0,3001))
msaEventInfoTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:msaEventInfoTrap.setStatus('')
msaEventWarningTrap=NotificationType((1,3,6,1,4,1,11,2,51,0,3002))
msaEventWarningTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:msaEventWarningTrap.setStatus('')
msaEventErrorTrap=NotificationType((1,3,6,1,4,1,11,2,51,0,3003))
msaEventErrorTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:msaEventErrorTrap.setStatus('')
msaEventCriticalTrap=NotificationType((1,3,6,1,4,1,11,2,51,0,3004))
msaEventCriticalTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:msaEventCriticalTrap.setStatus('')
msaEventResolvedTrap=NotificationType((1,3,6,1,4,1,11,2,51,0,3005))
msaEventResolvedTrap.setObjects(*((_A,_C),(_A,_D),(_A,_B)))
if mibBuilder.loadTexts:msaEventResolvedTrap.setStatus('')
mibBuilder.exportSymbols('MSA2000TRAPS-MIB',**{'hp':hp,'nm':nm,'hpMSA':hpMSA,'msaEventInfoTrap':msaEventInfoTrap,'msaEventWarningTrap':msaEventWarningTrap,'msaEventErrorTrap':msaEventErrorTrap,'msaEventCriticalTrap':msaEventCriticalTrap,'msaEventResolvedTrap':msaEventResolvedTrap,'mibName':mibName})
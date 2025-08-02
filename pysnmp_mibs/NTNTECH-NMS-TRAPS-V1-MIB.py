_F='NotificationType'
_E='mumStaFanState'
_D='NTNTECH-CHASSIS-STATUS-MIB'
_C='ifStaType'
_B='ifStaSlotIndex'
_A='NTNTECH-INTERFACE-MODULE-STATUS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mumStaFanState,=mibBuilder.importSymbols(_D,_E)
ifStaSlotIndex,ifStaType=mibBuilder.importSymbols(_A,_B,_C)
ntntechNMSTraps,=mibBuilder.importSymbols('NTNTECH-ROOT-MIB','ntntechNMSTraps')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_F,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_F,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
envFanTrap_v1=NotificationType((1,3,6,1,4,1,8059,1,3,0,1001))
envFanTrap_v1.setObjects((_D,_E))
if mibBuilder.loadTexts:envFanTrap_v1.setStatus('')
envTempNormal_v1=NotificationType((1,3,6,1,4,1,8059,1,3,0,1002))
if mibBuilder.loadTexts:envTempNormal_v1.setStatus('')
envTempExceeded_v1=NotificationType((1,3,6,1,4,1,8059,1,3,0,1003))
if mibBuilder.loadTexts:envTempExceeded_v1.setStatus('')
invIfModPresentTrap_v1=NotificationType((1,3,6,1,4,1,8059,1,3,0,2001))
invIfModPresentTrap_v1.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:invIfModPresentTrap_v1.setStatus('')
invIfModRemovedTrap_v1=NotificationType((1,3,6,1,4,1,8059,1,3,0,2002))
invIfModRemovedTrap_v1.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:invIfModRemovedTrap_v1.setStatus('')
mibBuilder.exportSymbols('NTNTECH-NMS-TRAPS-V1-MIB',**{'envFanTrap-v1':envFanTrap_v1,'envTempNormal-v1':envTempNormal_v1,'envTempExceeded-v1':envTempExceeded_v1,'invIfModPresentTrap-v1':invIfModPresentTrap_v1,'invIfModRemovedTrap-v1':invIfModRemovedTrap_v1})
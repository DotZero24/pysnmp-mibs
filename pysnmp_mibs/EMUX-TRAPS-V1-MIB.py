_G='EMUX-TRAPS-V1-MIB'
_F='NotificationType'
_E='e1SendStatus'
_D='e1RecvStatus'
_C='tdmLinkStatus'
_B='tdmAdminStatus'
_A='EMUX-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
e1RecvStatus,e1SendStatus,emux,tdmAdminStatus,tdmLinkStatus=mibBuilder.importSymbols(_A,_D,_E,'emux',_B,_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_F,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_F,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
e1LinkChangeV1=NotificationType((1,3,6,1,4,1,42926,2,0,1))
e1LinkChangeV1.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:e1LinkChangeV1.setStatus('')
tdmLinkDownV1=NotificationType((1,3,6,1,4,1,42926,2,0,2))
tdmLinkDownV1.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:tdmLinkDownV1.setStatus('')
tdmLinkUpV1=NotificationType((1,3,6,1,4,1,42926,2,0,3))
tdmLinkUpV1.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:tdmLinkUpV1.setStatus('')
trapDyingGasp=NotificationType((1,3,6,1,4,1,42926,2,0,6))
trapDyingGasp.setObjects((_G,'sysObjectID'))
if mibBuilder.loadTexts:trapDyingGasp.setStatus('')
mibBuilder.exportSymbols(_G,**{'e1LinkChangeV1':e1LinkChangeV1,'tdmLinkDownV1':tdmLinkDownV1,'tdmLinkUpV1':tdmLinkUpV1,'trapDyingGasp':trapDyingGasp})
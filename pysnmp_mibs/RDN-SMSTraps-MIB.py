_D='NotificationType'
_C='docsIfCmtsCmStatusValue'
_B='docsIfCmtsCmStatusMacAddress'
_A='DOCS-IF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
docsIfCmtsCmStatusMacAddress,docsIfCmtsCmStatusValue=mibBuilder.importSymbols(_A,_B,_C)
riverdelta,=mibBuilder.importSymbols('RDN-MIB','riverdelta')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_D,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_D,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_RdnSubscriberTraps_ObjectIdentity=ObjectIdentity
rdnSubscriberTraps=_RdnSubscriberTraps_ObjectIdentity((1,3,6,1,4,1,4981,5))
_RdnCableModemV1Traps_ObjectIdentity=ObjectIdentity
rdnCableModemV1Traps=_RdnCableModemV1Traps_ObjectIdentity((1,3,6,1,4,1,4981,5,1))
_RdnCableModemV2Traps_ObjectIdentity=ObjectIdentity
rdnCableModemV2Traps=_RdnCableModemV2Traps_ObjectIdentity((1,3,6,1,4,1,4981,5,2))
rdnCableModemStatusV1=NotificationType((1,3,6,1,4,1,4981,0,1))
rdnCableModemStatusV1.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:rdnCableModemStatusV1.setStatus('')
rdnCableModemStatusV2=NotificationType((1,3,6,1,4,1,4981,5,2,1))
rdnCableModemStatusV2.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:rdnCableModemStatusV2.setStatus('current')
mibBuilder.exportSymbols('RDN-SMSTraps-MIB',**{'rdnCableModemStatusV1':rdnCableModemStatusV1,'rdnSubscriberTraps':rdnSubscriberTraps,'rdnCableModemV1Traps':rdnCableModemV1Traps,'rdnCableModemV2Traps':rdnCableModemV2Traps,'rdnCableModemStatusV2':rdnCableModemStatusV2})
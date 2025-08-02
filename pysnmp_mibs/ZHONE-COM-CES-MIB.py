_E='zhoneAtmfCESDs0Bundle'
_D='zhoneAtmfCESConfExtEntry'
_C='ZHONE-COM-CES-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmfCESAdminStatus,atmfCESAtmIndex,atmfCESAtmVci,atmfCESAtmVpi,atmfCESBufMaxSize,atmfCESCas,atmfCESCbrClockMode,atmfCESCbrIndex,atmfCESCbrService,atmfCESCdvRxT,atmfCESCellLossIntegrationPeriod,atmfCESConfEntry,atmfCESConfRowStatus,atmfCESConnType,atmfCESLocalAddr,atmfCESOperStatus,atmfCESPartialFill=mibBuilder.importSymbols('ATMF-CES','atmfCESAdminStatus','atmfCESAtmIndex','atmfCESAtmVci','atmfCESAtmVpi','atmfCESBufMaxSize','atmfCESCas','atmfCESCbrClockMode','atmfCESCbrIndex','atmfCESCbrService','atmfCESCdvRxT','atmfCESCellLossIntegrationPeriod','atmfCESConfEntry','atmfCESConfRowStatus','atmfCESConnType','atmfCESLocalAddr','atmfCESOperStatus','atmfCESPartialFill')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zhoneCes,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneCes','zhoneModules')
comCesExtension=ModuleIdentity((1,3,6,1,4,1,5504,6,108))
if mibBuilder.loadTexts:comCesExtension.setRevisions(('2005-04-13 12:04','2004-08-16 12:00'))
_ZhoneAtmfCESConfExtTable_Object=MibTable
zhoneAtmfCESConfExtTable=_ZhoneAtmfCESConfExtTable_Object((1,3,6,1,4,1,5504,4,10,1))
if mibBuilder.loadTexts:zhoneAtmfCESConfExtTable.setStatus(_A)
_ZhoneAtmfCESConfExtEntry_Object=MibTableRow
zhoneAtmfCESConfExtEntry=_ZhoneAtmfCESConfExtEntry_Object((1,3,6,1,4,1,5504,4,10,1,1))
if mibBuilder.loadTexts:zhoneAtmfCESConfExtEntry.setStatus(_A)
class _ZhoneAtmfCESDs0Bundle_Type(Bits):namedValues=NamedValues(*(('ts0',0),('ts1',1),('ts2',2),('ts3',3),('ts4',4),('ts5',5),('ts6',6),('ts7',7),('ts8',8),('ts9',9),('ts10',10),('ts11',11),('ts12',12),('ts13',13),('ts14',14),('ts15',15),('ts16',16),('ts17',17),('ts18',18),('ts19',19),('ts20',20),('ts21',21),('ts22',22),('ts23',23),('ts24',24),('ts25',25),('ts26',26),('ts27',27),('ts28',28),('ts29',29),('ts30',30),('ts31',31)))
_ZhoneAtmfCESDs0Bundle_Type.__name__='Bits'
_ZhoneAtmfCESDs0Bundle_Object=MibTableColumn
zhoneAtmfCESDs0Bundle=_ZhoneAtmfCESDs0Bundle_Object((1,3,6,1,4,1,5504,4,10,1,1,1),_ZhoneAtmfCESDs0Bundle_Type())
zhoneAtmfCESDs0Bundle.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneAtmfCESDs0Bundle.setStatus(_A)
_ZhoneAtmfCESConfExtAtmfCESSrcIpAddr_Type=IpAddress
_ZhoneAtmfCESConfExtAtmfCESSrcIpAddr_Object=MibTableColumn
zhoneAtmfCESConfExtAtmfCESSrcIpAddr=_ZhoneAtmfCESConfExtAtmfCESSrcIpAddr_Object((1,3,6,1,4,1,5504,4,10,1,1,2),_ZhoneAtmfCESConfExtAtmfCESSrcIpAddr_Type())
zhoneAtmfCESConfExtAtmfCESSrcIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneAtmfCESConfExtAtmfCESSrcIpAddr.setStatus(_A)
_ZhoneAtmfCESConfExtAtmfCESDstIpAddr_Type=IpAddress
_ZhoneAtmfCESConfExtAtmfCESDstIpAddr_Object=MibTableColumn
zhoneAtmfCESConfExtAtmfCESDstIpAddr=_ZhoneAtmfCESConfExtAtmfCESDstIpAddr_Object((1,3,6,1,4,1,5504,4,10,1,1,3),_ZhoneAtmfCESConfExtAtmfCESDstIpAddr_Type())
zhoneAtmfCESConfExtAtmfCESDstIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneAtmfCESConfExtAtmfCESDstIpAddr.setStatus(_A)
_ZhoneAtmfCESConfExtAtmfCESSrcPort_Type=Unsigned32
_ZhoneAtmfCESConfExtAtmfCESSrcPort_Object=MibTableColumn
zhoneAtmfCESConfExtAtmfCESSrcPort=_ZhoneAtmfCESConfExtAtmfCESSrcPort_Object((1,3,6,1,4,1,5504,4,10,1,1,4),_ZhoneAtmfCESConfExtAtmfCESSrcPort_Type())
zhoneAtmfCESConfExtAtmfCESSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneAtmfCESConfExtAtmfCESSrcPort.setStatus(_A)
_ZhoneAtmfCESConfExtAtmfCESDstPort_Type=Unsigned32
_ZhoneAtmfCESConfExtAtmfCESDstPort_Object=MibTableColumn
zhoneAtmfCESConfExtAtmfCESDstPort=_ZhoneAtmfCESConfExtAtmfCESDstPort_Object((1,3,6,1,4,1,5504,4,10,1,1,5),_ZhoneAtmfCESConfExtAtmfCESDstPort_Type())
zhoneAtmfCESConfExtAtmfCESDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneAtmfCESConfExtAtmfCESDstPort.setStatus(_A)
atmfCESConfEntry.registerAugmentions((_C,_D))
zhoneAtmfCESConfExtEntry.setIndexNames(*atmfCESConfEntry.getIndexNames())
zhoneAtmfCESGroup=ObjectGroup((1,3,6,1,4,1,5504,4,10,2))
zhoneAtmfCESGroup.setObjects((_C,_E))
if mibBuilder.loadTexts:zhoneAtmfCESGroup.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zhoneAtmfCESConfExtTable':zhoneAtmfCESConfExtTable,_D:zhoneAtmfCESConfExtEntry,_E:zhoneAtmfCESDs0Bundle,'zhoneAtmfCESConfExtAtmfCESSrcIpAddr':zhoneAtmfCESConfExtAtmfCESSrcIpAddr,'zhoneAtmfCESConfExtAtmfCESDstIpAddr':zhoneAtmfCESConfExtAtmfCESDstIpAddr,'zhoneAtmfCESConfExtAtmfCESSrcPort':zhoneAtmfCESConfExtAtmfCESSrcPort,'zhoneAtmfCESConfExtAtmfCESDstPort':zhoneAtmfCESConfExtAtmfCESDstPort,'zhoneAtmfCESGroup':zhoneAtmfCESGroup,'comCesExtension':comCesExtension})
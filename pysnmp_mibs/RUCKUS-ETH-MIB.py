_D='ruckusEthIndex'
_C='RUCKUS-ETH-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ruckusCommonEthModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusCommonEthModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
ruckusEthMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,1,13,1))
_RuckusEthObjects_ObjectIdentity=ObjectIdentity
ruckusEthObjects=_RuckusEthObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,1,13,1,1))
_RuckusEthInfo_ObjectIdentity=ObjectIdentity
ruckusEthInfo=_RuckusEthInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,13,1,1,1))
_RuckusEthStatsTable_Object=MibTable
ruckusEthStatsTable=_RuckusEthStatsTable_Object((1,3,6,1,4,1,25053,1,1,13,1,1,1,1))
if mibBuilder.loadTexts:ruckusEthStatsTable.setStatus(_A)
_RuckusEthStatsEntry_Object=MibTableRow
ruckusEthStatsEntry=_RuckusEthStatsEntry_Object((1,3,6,1,4,1,25053,1,1,13,1,1,1,1,1))
ruckusEthStatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ruckusEthStatsEntry.setStatus(_A)
_RuckusEthName_Type=DisplayString
_RuckusEthName_Object=MibTableColumn
ruckusEthName=_RuckusEthName_Object((1,3,6,1,4,1,25053,1,1,13,1,1,1,1,1,1),_RuckusEthName_Type())
ruckusEthName.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusEthName.setStatus(_A)
_RuckusEthStatsRxRate_Type=Counter32
_RuckusEthStatsRxRate_Object=MibTableColumn
ruckusEthStatsRxRate=_RuckusEthStatsRxRate_Object((1,3,6,1,4,1,25053,1,1,13,1,1,1,1,1,2),_RuckusEthStatsRxRate_Type())
ruckusEthStatsRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusEthStatsRxRate.setStatus(_A)
_RuckusEthStatsRxErrorRate_Type=Counter32
_RuckusEthStatsRxErrorRate_Object=MibTableColumn
ruckusEthStatsRxErrorRate=_RuckusEthStatsRxErrorRate_Object((1,3,6,1,4,1,25053,1,1,13,1,1,1,1,1,3),_RuckusEthStatsRxErrorRate_Type())
ruckusEthStatsRxErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusEthStatsRxErrorRate.setStatus(_A)
_RuckusEthStatsTxRate_Type=Counter32
_RuckusEthStatsTxRate_Object=MibTableColumn
ruckusEthStatsTxRate=_RuckusEthStatsTxRate_Object((1,3,6,1,4,1,25053,1,1,13,1,1,1,1,1,4),_RuckusEthStatsTxRate_Type())
ruckusEthStatsTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusEthStatsTxRate.setStatus(_A)
_RuckusEthStatsTxErrorRate_Type=Counter32
_RuckusEthStatsTxErrorRate_Object=MibTableColumn
ruckusEthStatsTxErrorRate=_RuckusEthStatsTxErrorRate_Object((1,3,6,1,4,1,25053,1,1,13,1,1,1,1,1,5),_RuckusEthStatsTxErrorRate_Type())
ruckusEthStatsTxErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusEthStatsTxErrorRate.setStatus(_A)
_RuckusEthIndex_Type=InterfaceIndex
_RuckusEthIndex_Object=MibTableColumn
ruckusEthIndex=_RuckusEthIndex_Object((1,3,6,1,4,1,25053,1,1,13,1,1,1,1,1,200),_RuckusEthIndex_Type())
ruckusEthIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusEthIndex.setStatus(_A)
_RuckusEthEvents_ObjectIdentity=ObjectIdentity
ruckusEthEvents=_RuckusEthEvents_ObjectIdentity((1,3,6,1,4,1,25053,1,1,13,1,2))
mibBuilder.exportSymbols(_C,**{'ruckusEthMIB':ruckusEthMIB,'ruckusEthObjects':ruckusEthObjects,'ruckusEthInfo':ruckusEthInfo,'ruckusEthStatsTable':ruckusEthStatsTable,'ruckusEthStatsEntry':ruckusEthStatsEntry,'ruckusEthName':ruckusEthName,'ruckusEthStatsRxRate':ruckusEthStatsRxRate,'ruckusEthStatsRxErrorRate':ruckusEthStatsRxErrorRate,'ruckusEthStatsTxRate':ruckusEthStatsTxRate,'ruckusEthStatsTxErrorRate':ruckusEthStatsTxErrorRate,_D:ruckusEthIndex,'ruckusEthEvents':ruckusEthEvents})
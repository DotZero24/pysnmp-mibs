_O='dwCtpGroup'
_N='dwCtpOprCarrierCtpList'
_M='dwCtpPropagationDelay'
_L='dwCtpTotalBW'
_K='dwCtpRxTTI'
_J='dwCtpExpTTI'
_I='dwCtpTxTTI'
_H='dwCtpCarrierCtpList'
_G='dwCtpMoID'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-DWCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatArbitraryPrecision,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dwCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,64))
if mibBuilder.loadTexts:dwCtpMIB.setRevisions(('2017-01-13 00:00',))
_DwCtpTable_Object=MibTable
dwCtpTable=_DwCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,64,1))
if mibBuilder.loadTexts:dwCtpTable.setStatus(_A)
_DwCtpEntry_Object=MibTableRow
dwCtpEntry=_DwCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,64,1,1))
dwCtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dwCtpEntry.setStatus(_A)
_DwCtpMoID_Type=DisplayString
_DwCtpMoID_Object=MibTableColumn
dwCtpMoID=_DwCtpMoID_Object((1,3,6,1,4,1,21296,2,2,2,2,64,1,1,1),_DwCtpMoID_Type())
dwCtpMoID.setMaxAccess('read-create')
if mibBuilder.loadTexts:dwCtpMoID.setStatus(_A)
_DwCtpCarrierCtpList_Type=DisplayString
_DwCtpCarrierCtpList_Object=MibTableColumn
dwCtpCarrierCtpList=_DwCtpCarrierCtpList_Object((1,3,6,1,4,1,21296,2,2,2,2,64,1,1,2),_DwCtpCarrierCtpList_Type())
dwCtpCarrierCtpList.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpCarrierCtpList.setStatus(_A)
_DwCtpTxTTI_Type=DisplayString
_DwCtpTxTTI_Object=MibTableColumn
dwCtpTxTTI=_DwCtpTxTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,64,1,1,3),_DwCtpTxTTI_Type())
dwCtpTxTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpTxTTI.setStatus(_A)
_DwCtpExpTTI_Type=DisplayString
_DwCtpExpTTI_Object=MibTableColumn
dwCtpExpTTI=_DwCtpExpTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,64,1,1,4),_DwCtpExpTTI_Type())
dwCtpExpTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpExpTTI.setStatus(_A)
_DwCtpRxTTI_Type=DisplayString
_DwCtpRxTTI_Object=MibTableColumn
dwCtpRxTTI=_DwCtpRxTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,64,1,1,5),_DwCtpRxTTI_Type())
dwCtpRxTTI.setMaxAccess(_D)
if mibBuilder.loadTexts:dwCtpRxTTI.setStatus(_A)
_DwCtpTotalBW_Type=Unsigned32
_DwCtpTotalBW_Object=MibTableColumn
dwCtpTotalBW=_DwCtpTotalBW_Object((1,3,6,1,4,1,21296,2,2,2,2,64,1,1,6),_DwCtpTotalBW_Type())
dwCtpTotalBW.setMaxAccess(_D)
if mibBuilder.loadTexts:dwCtpTotalBW.setStatus(_A)
_DwCtpPropagationDelay_Type=FloatArbitraryPrecision
_DwCtpPropagationDelay_Object=MibTableColumn
dwCtpPropagationDelay=_DwCtpPropagationDelay_Object((1,3,6,1,4,1,21296,2,2,2,2,64,1,1,7),_DwCtpPropagationDelay_Type())
dwCtpPropagationDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:dwCtpPropagationDelay.setStatus(_A)
_DwCtpOprCarrierCtpList_Type=DisplayString
_DwCtpOprCarrierCtpList_Object=MibTableColumn
dwCtpOprCarrierCtpList=_DwCtpOprCarrierCtpList_Object((1,3,6,1,4,1,21296,2,2,2,2,64,1,1,8),_DwCtpOprCarrierCtpList_Type())
dwCtpOprCarrierCtpList.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpOprCarrierCtpList.setStatus(_A)
_DwCtpConformance_ObjectIdentity=ObjectIdentity
dwCtpConformance=_DwCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,64,3))
_DwCtpCompliances_ObjectIdentity=ObjectIdentity
dwCtpCompliances=_DwCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,64,3,1))
_DwCtpGroups_ObjectIdentity=ObjectIdentity
dwCtpGroups=_DwCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,64,3,2))
dwCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,64,3,2,1))
dwCtpGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:dwCtpGroup.setStatus(_A)
dwCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,64,3,1,1))
dwCtpCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:dwCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dwCtpMIB':dwCtpMIB,'dwCtpTable':dwCtpTable,'dwCtpEntry':dwCtpEntry,_G:dwCtpMoID,_H:dwCtpCarrierCtpList,_I:dwCtpTxTTI,_J:dwCtpExpTTI,_K:dwCtpRxTTI,_L:dwCtpTotalBW,_M:dwCtpPropagationDelay,_N:dwCtpOprCarrierCtpList,'dwCtpConformance':dwCtpConformance,'dwCtpCompliances':dwCtpCompliances,'dwCtpCompliance':dwCtpCompliance,'dwCtpGroups':dwCtpGroups,_O:dwCtpGroup})
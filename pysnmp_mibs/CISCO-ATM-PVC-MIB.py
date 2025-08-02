_R='ciscoAtmPvcMIBGroup'
_Q='capvcRowStatus'
_P='capvcVlanId'
_O='capvcFrequency'
_N='capvcOAM'
_M='capvcPCR'
_L='capvcType'
_K='capvcVCD'
_J='capvcVCI'
_I='capvcVPI'
_H='capvcPort'
_G='TruthValue'
_F='Integer32'
_E='not-accessible'
_D='read-create'
_C='Unsigned32'
_B='CISCO-ATM-PVC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_G)
ciscoAtmPvcMIB=ModuleIdentity((1,3,6,1,4,1,9,9,94))
if mibBuilder.loadTexts:ciscoAtmPvcMIB.setRevisions(('2002-04-11 00:00','1997-11-18 00:00'))
_CiscoAtmPvcMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAtmPvcMIBObjects=_CiscoAtmPvcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,94,1))
_CiscoAtmPvcCreateBindGroup_ObjectIdentity=ObjectIdentity
ciscoAtmPvcCreateBindGroup=_CiscoAtmPvcCreateBindGroup_ObjectIdentity((1,3,6,1,4,1,9,9,94,1,1))
_CapvcTable_Object=MibTable
capvcTable=_CapvcTable_Object((1,3,6,1,4,1,9,9,94,1,1,1))
if mibBuilder.loadTexts:capvcTable.setStatus(_A)
_CapvcEntry_Object=MibTableRow
capvcEntry=_CapvcEntry_Object((1,3,6,1,4,1,9,9,94,1,1,1,1))
capvcEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:capvcEntry.setStatus(_A)
_CapvcPort_Type=Unsigned32
_CapvcPort_Object=MibTableColumn
capvcPort=_CapvcPort_Object((1,3,6,1,4,1,9,9,94,1,1,1,1,1),_CapvcPort_Type())
capvcPort.setMaxAccess(_E)
if mibBuilder.loadTexts:capvcPort.setStatus(_A)
class _CapvcVPI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CapvcVPI_Type.__name__=_C
_CapvcVPI_Object=MibTableColumn
capvcVPI=_CapvcVPI_Object((1,3,6,1,4,1,9,9,94,1,1,1,1,2),_CapvcVPI_Type())
capvcVPI.setMaxAccess(_E)
if mibBuilder.loadTexts:capvcVPI.setStatus(_A)
class _CapvcVCI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CapvcVCI_Type.__name__=_C
_CapvcVCI_Object=MibTableColumn
capvcVCI=_CapvcVCI_Object((1,3,6,1,4,1,9,9,94,1,1,1,1,3),_CapvcVCI_Type())
capvcVCI.setMaxAccess(_E)
if mibBuilder.loadTexts:capvcVCI.setStatus(_A)
class _CapvcVCD_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CapvcVCD_Type.__name__=_C
_CapvcVCD_Object=MibTableColumn
capvcVCD=_CapvcVCD_Object((1,3,6,1,4,1,9,9,94,1,1,1,1,4),_CapvcVCD_Type())
capvcVCD.setMaxAccess('read-only')
if mibBuilder.loadTexts:capvcVCD.setStatus(_A)
class _CapvcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('aal5snap',1),('ilmi',2),('qsaal',3)))
_CapvcType_Type.__name__=_F
_CapvcType_Object=MibTableColumn
capvcType=_CapvcType_Object((1,3,6,1,4,1,9,9,94,1,1,1,1,5),_CapvcType_Type())
capvcType.setMaxAccess(_D)
if mibBuilder.loadTexts:capvcType.setStatus(_A)
class _CapvcPCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,155000))
_CapvcPCR_Type.__name__=_C
_CapvcPCR_Object=MibTableColumn
capvcPCR=_CapvcPCR_Object((1,3,6,1,4,1,9,9,94,1,1,1,1,6),_CapvcPCR_Type())
capvcPCR.setMaxAccess(_D)
if mibBuilder.loadTexts:capvcPCR.setStatus(_A)
if mibBuilder.loadTexts:capvcPCR.setUnits('kbps')
class _CapvcOAM_Type(TruthValue):defaultValue=2
_CapvcOAM_Type.__name__=_G
_CapvcOAM_Object=MibTableColumn
capvcOAM=_CapvcOAM_Object((1,3,6,1,4,1,9,9,94,1,1,1,1,7),_CapvcOAM_Type())
capvcOAM.setMaxAccess(_D)
if mibBuilder.loadTexts:capvcOAM.setStatus(_A)
class _CapvcFrequency_Type(Unsigned32):defaultValue=10
_CapvcFrequency_Type.__name__=_C
_CapvcFrequency_Object=MibTableColumn
capvcFrequency=_CapvcFrequency_Object((1,3,6,1,4,1,9,9,94,1,1,1,1,8),_CapvcFrequency_Type())
capvcFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:capvcFrequency.setStatus(_A)
if mibBuilder.loadTexts:capvcFrequency.setUnits('seconds')
class _CapvcVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CapvcVlanId_Type.__name__=_C
_CapvcVlanId_Object=MibTableColumn
capvcVlanId=_CapvcVlanId_Object((1,3,6,1,4,1,9,9,94,1,1,1,1,9),_CapvcVlanId_Type())
capvcVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:capvcVlanId.setStatus(_A)
_CapvcRowStatus_Type=RowStatus
_CapvcRowStatus_Object=MibTableColumn
capvcRowStatus=_CapvcRowStatus_Object((1,3,6,1,4,1,9,9,94,1,1,1,1,10),_CapvcRowStatus_Type())
capvcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:capvcRowStatus.setStatus(_A)
_CiscoAtmPvcMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAtmPvcMIBConformance=_CiscoAtmPvcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,94,3))
_CiscoAtmPvcMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAtmPvcMIBCompliances=_CiscoAtmPvcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,94,3,1))
_CiscoAtmPvcMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAtmPvcMIBGroups=_CiscoAtmPvcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,94,3,2))
ciscoAtmPvcMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,94,3,2,1))
ciscoAtmPvcMIBGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoAtmPvcMIBGroup.setStatus(_A)
ciscoAtmPvcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,94,3,1,1))
ciscoAtmPvcMIBCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:ciscoAtmPvcMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoAtmPvcMIB':ciscoAtmPvcMIB,'ciscoAtmPvcMIBObjects':ciscoAtmPvcMIBObjects,'ciscoAtmPvcCreateBindGroup':ciscoAtmPvcCreateBindGroup,'capvcTable':capvcTable,'capvcEntry':capvcEntry,_H:capvcPort,_I:capvcVPI,_J:capvcVCI,_K:capvcVCD,_L:capvcType,_M:capvcPCR,_N:capvcOAM,_O:capvcFrequency,_P:capvcVlanId,_Q:capvcRowStatus,'ciscoAtmPvcMIBConformance':ciscoAtmPvcMIBConformance,'ciscoAtmPvcMIBCompliances':ciscoAtmPvcMIBCompliances,'ciscoAtmPvcMIBCompliance':ciscoAtmPvcMIBCompliance,'ciscoAtmPvcMIBGroups':ciscoAtmPvcMIBGroups,_R:ciscoAtmPvcMIBGroup})
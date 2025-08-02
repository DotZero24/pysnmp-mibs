_H='panSystemVolServiceVolIndex'
_G='panSystemClusterRepsetEntryIndex'
_F='DisplayString'
_E='panSystemServicesId'
_D='Integer32'
_C='PANASAS-SYSTEM-MIB-V1'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
panFs,=mibBuilder.importSymbols('PANASAS-PANFS-MIB-V1','panFs')
PanSerialNumber,=mibBuilder.importSymbols('PANASAS-TC-MIB','PanSerialNumber')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
panSystem=ModuleIdentity((1,3,6,1,4,1,10159,1,3,2))
if mibBuilder.loadTexts:panSystem.setRevisions(('2011-04-07 00:00',))
_PanSystemCluster_ObjectIdentity=ObjectIdentity
panSystemCluster=_PanSystemCluster_ObjectIdentity((1,3,6,1,4,1,10159,1,3,2,1))
class _PanSystemClusterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PanSystemClusterName_Type.__name__=_F
_PanSystemClusterName_Object=MibScalar
panSystemClusterName=_PanSystemClusterName_Object((1,3,6,1,4,1,10159,1,3,2,1,1),_PanSystemClusterName_Type())
panSystemClusterName.setMaxAccess(_B)
if mibBuilder.loadTexts:panSystemClusterName.setStatus(_A)
_PanSystemClusterManagementAddress_Type=IpAddress
_PanSystemClusterManagementAddress_Object=MibScalar
panSystemClusterManagementAddress=_PanSystemClusterManagementAddress_Object((1,3,6,1,4,1,10159,1,3,2,1,2),_PanSystemClusterManagementAddress_Type())
panSystemClusterManagementAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:panSystemClusterManagementAddress.setStatus(_A)
_PanSystemClusterRepsetTable_Object=MibTable
panSystemClusterRepsetTable=_PanSystemClusterRepsetTable_Object((1,3,6,1,4,1,10159,1,3,2,1,3))
if mibBuilder.loadTexts:panSystemClusterRepsetTable.setStatus(_A)
_PanSystemClusterRepsetEntry_Object=MibTableRow
panSystemClusterRepsetEntry=_PanSystemClusterRepsetEntry_Object((1,3,6,1,4,1,10159,1,3,2,1,3,1))
panSystemClusterRepsetEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:panSystemClusterRepsetEntry.setStatus(_A)
class _PanSystemClusterRepsetEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_PanSystemClusterRepsetEntryIndex_Type.__name__=_D
_PanSystemClusterRepsetEntryIndex_Object=MibTableColumn
panSystemClusterRepsetEntryIndex=_PanSystemClusterRepsetEntryIndex_Object((1,3,6,1,4,1,10159,1,3,2,1,3,1,1),_PanSystemClusterRepsetEntryIndex_Type())
panSystemClusterRepsetEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:panSystemClusterRepsetEntryIndex.setStatus(_A)
_PanSystemClusterRepsetEntryIpAddr_Type=IpAddress
_PanSystemClusterRepsetEntryIpAddr_Object=MibTableColumn
panSystemClusterRepsetEntryIpAddr=_PanSystemClusterRepsetEntryIpAddr_Object((1,3,6,1,4,1,10159,1,3,2,1,3,1,2),_PanSystemClusterRepsetEntryIpAddr_Type())
panSystemClusterRepsetEntryIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:panSystemClusterRepsetEntryIpAddr.setStatus(_A)
_PanSystemClusterRepsetEntryBladeHwSN_Type=PanSerialNumber
_PanSystemClusterRepsetEntryBladeHwSN_Object=MibTableColumn
panSystemClusterRepsetEntryBladeHwSN=_PanSystemClusterRepsetEntryBladeHwSN_Object((1,3,6,1,4,1,10159,1,3,2,1,3,1,3),_PanSystemClusterRepsetEntryBladeHwSN_Type())
panSystemClusterRepsetEntryBladeHwSN.setMaxAccess(_B)
if mibBuilder.loadTexts:panSystemClusterRepsetEntryBladeHwSN.setStatus(_A)
_PanSystemServicesTable_Object=MibTable
panSystemServicesTable=_PanSystemServicesTable_Object((1,3,6,1,4,1,10159,1,3,2,2))
if mibBuilder.loadTexts:panSystemServicesTable.setStatus(_A)
_PanSystemServicesEntry_Object=MibTableRow
panSystemServicesEntry=_PanSystemServicesEntry_Object((1,3,6,1,4,1,10159,1,3,2,2,1))
panSystemServicesEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:panSystemServicesEntry.setStatus(_A)
_PanSystemServicesId_Type=PanSerialNumber
_PanSystemServicesId_Object=MibTableColumn
panSystemServicesId=_PanSystemServicesId_Object((1,3,6,1,4,1,10159,1,3,2,2,1,1),_PanSystemServicesId_Type())
panSystemServicesId.setMaxAccess(_B)
if mibBuilder.loadTexts:panSystemServicesId.setStatus(_A)
_PanSystemServicesBladeHwSN_Type=PanSerialNumber
_PanSystemServicesBladeHwSN_Object=MibTableColumn
panSystemServicesBladeHwSN=_PanSystemServicesBladeHwSN_Object((1,3,6,1,4,1,10159,1,3,2,2,1,2),_PanSystemServicesBladeHwSN_Type())
panSystemServicesBladeHwSN.setMaxAccess(_B)
if mibBuilder.loadTexts:panSystemServicesBladeHwSN.setStatus(_A)
_PanSystemServicesType_Type=DisplayString
_PanSystemServicesType_Object=MibTableColumn
panSystemServicesType=_PanSystemServicesType_Object((1,3,6,1,4,1,10159,1,3,2,2,1,3),_PanSystemServicesType_Type())
panSystemServicesType.setMaxAccess(_B)
if mibBuilder.loadTexts:panSystemServicesType.setStatus(_A)
_PanSystemServicesInfo_Type=DisplayString
_PanSystemServicesInfo_Object=MibTableColumn
panSystemServicesInfo=_PanSystemServicesInfo_Object((1,3,6,1,4,1,10159,1,3,2,2,1,4),_PanSystemServicesInfo_Type())
panSystemServicesInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:panSystemServicesInfo.setStatus(_A)
_PanSystemServicesBackupBladeHwSN_Type=PanSerialNumber
_PanSystemServicesBackupBladeHwSN_Object=MibTableColumn
panSystemServicesBackupBladeHwSN=_PanSystemServicesBackupBladeHwSN_Object((1,3,6,1,4,1,10159,1,3,2,2,1,5),_PanSystemServicesBackupBladeHwSN_Type())
panSystemServicesBackupBladeHwSN.setMaxAccess(_B)
if mibBuilder.loadTexts:panSystemServicesBackupBladeHwSN.setStatus(_A)
_PanSystemVolServiceTable_Object=MibTable
panSystemVolServiceTable=_PanSystemVolServiceTable_Object((1,3,6,1,4,1,10159,1,3,2,3))
if mibBuilder.loadTexts:panSystemVolServiceTable.setStatus(_A)
_PanSystemVolServiceEntry_Object=MibTableRow
panSystemVolServiceEntry=_PanSystemVolServiceEntry_Object((1,3,6,1,4,1,10159,1,3,2,3,1))
panSystemVolServiceEntry.setIndexNames((0,_C,_E),(0,_C,_H))
if mibBuilder.loadTexts:panSystemVolServiceEntry.setStatus(_A)
class _PanSystemVolServiceVolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_PanSystemVolServiceVolIndex_Type.__name__=_D
_PanSystemVolServiceVolIndex_Object=MibTableColumn
panSystemVolServiceVolIndex=_PanSystemVolServiceVolIndex_Object((1,3,6,1,4,1,10159,1,3,2,3,1,1),_PanSystemVolServiceVolIndex_Type())
panSystemVolServiceVolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:panSystemVolServiceVolIndex.setStatus(_A)
_PanSystemVolServiceVolPath_Type=DisplayString
_PanSystemVolServiceVolPath_Object=MibTableColumn
panSystemVolServiceVolPath=_PanSystemVolServiceVolPath_Object((1,3,6,1,4,1,10159,1,3,2,3,1,2),_PanSystemVolServiceVolPath_Type())
panSystemVolServiceVolPath.setMaxAccess(_B)
if mibBuilder.loadTexts:panSystemVolServiceVolPath.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'panSystem':panSystem,'panSystemCluster':panSystemCluster,'panSystemClusterName':panSystemClusterName,'panSystemClusterManagementAddress':panSystemClusterManagementAddress,'panSystemClusterRepsetTable':panSystemClusterRepsetTable,'panSystemClusterRepsetEntry':panSystemClusterRepsetEntry,_G:panSystemClusterRepsetEntryIndex,'panSystemClusterRepsetEntryIpAddr':panSystemClusterRepsetEntryIpAddr,'panSystemClusterRepsetEntryBladeHwSN':panSystemClusterRepsetEntryBladeHwSN,'panSystemServicesTable':panSystemServicesTable,'panSystemServicesEntry':panSystemServicesEntry,_E:panSystemServicesId,'panSystemServicesBladeHwSN':panSystemServicesBladeHwSN,'panSystemServicesType':panSystemServicesType,'panSystemServicesInfo':panSystemServicesInfo,'panSystemServicesBackupBladeHwSN':panSystemServicesBackupBladeHwSN,'panSystemVolServiceTable':panSystemVolServiceTable,'panSystemVolServiceEntry':panSystemVolServiceEntry,_H:panSystemVolServiceVolIndex,'panSystemVolServiceVolPath':panSystemVolServiceVolPath})
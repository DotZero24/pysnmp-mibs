_N='read-write'
_M='nbsPartProgPartIndex'
_L='nbsPartProgIfIndex'
_K='nbsPartFirmPartIndex'
_J='nbsPartFirmIfIndex'
_I='nbsPartHardPartIndex'
_H='nbsPartHardIfIndex'
_G='Integer32'
_F='OctetString'
_E='not-accessible'
_D='NBS-PART-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
NbsTcPartIndex,nbs=mibBuilder.importSymbols('NBS-MIB','NbsTcPartIndex','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
nbsPartMib=ModuleIdentity((1,3,6,1,4,1,629,231))
_NbsPartHardGrp_ObjectIdentity=ObjectIdentity
nbsPartHardGrp=_NbsPartHardGrp_ObjectIdentity((1,3,6,1,4,1,629,231,1))
if mibBuilder.loadTexts:nbsPartHardGrp.setStatus(_A)
_NbsPartHardTable_Object=MibTable
nbsPartHardTable=_NbsPartHardTable_Object((1,3,6,1,4,1,629,231,1,1))
if mibBuilder.loadTexts:nbsPartHardTable.setStatus(_A)
_NbsPartHardEntry_Object=MibTableRow
nbsPartHardEntry=_NbsPartHardEntry_Object((1,3,6,1,4,1,629,231,1,1,1))
nbsPartHardEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:nbsPartHardEntry.setStatus(_A)
_NbsPartHardIfIndex_Type=InterfaceIndex
_NbsPartHardIfIndex_Object=MibTableColumn
nbsPartHardIfIndex=_NbsPartHardIfIndex_Object((1,3,6,1,4,1,629,231,1,1,1,1),_NbsPartHardIfIndex_Type())
nbsPartHardIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsPartHardIfIndex.setStatus(_A)
_NbsPartHardPartIndex_Type=NbsTcPartIndex
_NbsPartHardPartIndex_Object=MibTableColumn
nbsPartHardPartIndex=_NbsPartHardPartIndex_Object((1,3,6,1,4,1,629,231,1,1,1,2),_NbsPartHardPartIndex_Type())
nbsPartHardPartIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsPartHardPartIndex.setStatus(_A)
class _NbsPartHardDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NbsPartHardDescription_Type.__name__=_C
_NbsPartHardDescription_Object=MibTableColumn
nbsPartHardDescription=_NbsPartHardDescription_Object((1,3,6,1,4,1,629,231,1,1,1,10),_NbsPartHardDescription_Type())
nbsPartHardDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartHardDescription.setStatus(_A)
class _NbsPartHardSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NbsPartHardSerialNumber_Type.__name__=_C
_NbsPartHardSerialNumber_Object=MibTableColumn
nbsPartHardSerialNumber=_NbsPartHardSerialNumber_Object((1,3,6,1,4,1,629,231,1,1,1,11),_NbsPartHardSerialNumber_Type())
nbsPartHardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartHardSerialNumber.setStatus(_A)
class _NbsPartHardProductionId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsPartHardProductionId_Type.__name__=_C
_NbsPartHardProductionId_Object=MibTableColumn
nbsPartHardProductionId=_NbsPartHardProductionId_Object((1,3,6,1,4,1,629,231,1,1,1,20),_NbsPartHardProductionId_Type())
nbsPartHardProductionId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartHardProductionId.setStatus(_A)
class _NbsPartHardVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsPartHardVendor_Type.__name__=_C
_NbsPartHardVendor_Object=MibTableColumn
nbsPartHardVendor=_NbsPartHardVendor_Object((1,3,6,1,4,1,629,231,1,1,1,30),_NbsPartHardVendor_Type())
nbsPartHardVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartHardVendor.setStatus(_A)
class _NbsPartHardModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NbsPartHardModel_Type.__name__=_C
_NbsPartHardModel_Object=MibTableColumn
nbsPartHardModel=_NbsPartHardModel_Object((1,3,6,1,4,1,629,231,1,1,1,31),_NbsPartHardModel_Type())
nbsPartHardModel.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartHardModel.setStatus(_A)
class _NbsPartHardWareRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsPartHardWareRev_Type.__name__=_C
_NbsPartHardWareRev_Object=MibTableColumn
nbsPartHardWareRev=_NbsPartHardWareRev_Object((1,3,6,1,4,1,629,231,1,1,1,32),_NbsPartHardWareRev_Type())
nbsPartHardWareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartHardWareRev.setStatus(_A)
_NbsPartFirmGrp_ObjectIdentity=ObjectIdentity
nbsPartFirmGrp=_NbsPartFirmGrp_ObjectIdentity((1,3,6,1,4,1,629,231,2))
if mibBuilder.loadTexts:nbsPartFirmGrp.setStatus(_A)
_NbsPartFirmTable_Object=MibTable
nbsPartFirmTable=_NbsPartFirmTable_Object((1,3,6,1,4,1,629,231,2,1))
if mibBuilder.loadTexts:nbsPartFirmTable.setStatus(_A)
_NbsPartFirmEntry_Object=MibTableRow
nbsPartFirmEntry=_NbsPartFirmEntry_Object((1,3,6,1,4,1,629,231,2,1,1))
nbsPartFirmEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:nbsPartFirmEntry.setStatus(_A)
_NbsPartFirmIfIndex_Type=InterfaceIndex
_NbsPartFirmIfIndex_Object=MibTableColumn
nbsPartFirmIfIndex=_NbsPartFirmIfIndex_Object((1,3,6,1,4,1,629,231,2,1,1,1),_NbsPartFirmIfIndex_Type())
nbsPartFirmIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsPartFirmIfIndex.setStatus(_A)
_NbsPartFirmPartIndex_Type=NbsTcPartIndex
_NbsPartFirmPartIndex_Object=MibTableColumn
nbsPartFirmPartIndex=_NbsPartFirmPartIndex_Object((1,3,6,1,4,1,629,231,2,1,1,2),_NbsPartFirmPartIndex_Type())
nbsPartFirmPartIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsPartFirmPartIndex.setStatus(_A)
class _NbsPartFirmFpgaRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsPartFirmFpgaRev_Type.__name__=_C
_NbsPartFirmFpgaRev_Object=MibTableColumn
nbsPartFirmFpgaRev=_NbsPartFirmFpgaRev_Object((1,3,6,1,4,1,629,231,2,1,1,13),_NbsPartFirmFpgaRev_Type())
nbsPartFirmFpgaRev.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartFirmFpgaRev.setStatus(_A)
_NbsPartFirmSwMajor_Type=Integer32
_NbsPartFirmSwMajor_Object=MibTableColumn
nbsPartFirmSwMajor=_NbsPartFirmSwMajor_Object((1,3,6,1,4,1,629,231,2,1,1,14),_NbsPartFirmSwMajor_Type())
nbsPartFirmSwMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartFirmSwMajor.setStatus(_A)
_NbsPartFirmSwMinor_Type=Integer32
_NbsPartFirmSwMinor_Object=MibTableColumn
nbsPartFirmSwMinor=_NbsPartFirmSwMinor_Object((1,3,6,1,4,1,629,231,2,1,1,15),_NbsPartFirmSwMinor_Type())
nbsPartFirmSwMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartFirmSwMinor.setStatus(_A)
_NbsPartFirmSwBuild_Type=Integer32
_NbsPartFirmSwBuild_Object=MibTableColumn
nbsPartFirmSwBuild=_NbsPartFirmSwBuild_Object((1,3,6,1,4,1,629,231,2,1,1,16),_NbsPartFirmSwBuild_Type())
nbsPartFirmSwBuild.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartFirmSwBuild.setStatus(_A)
_NbsPartFirmWareIndex_Type=Integer32
_NbsPartFirmWareIndex_Object=MibTableColumn
nbsPartFirmWareIndex=_NbsPartFirmWareIndex_Object((1,3,6,1,4,1,629,231,2,1,1,30),_NbsPartFirmWareIndex_Type())
nbsPartFirmWareIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartFirmWareIndex.setStatus(_A)
_NbsPartProgGrp_ObjectIdentity=ObjectIdentity
nbsPartProgGrp=_NbsPartProgGrp_ObjectIdentity((1,3,6,1,4,1,629,231,3))
if mibBuilder.loadTexts:nbsPartProgGrp.setStatus(_A)
_NbsPartProgTable_Object=MibTable
nbsPartProgTable=_NbsPartProgTable_Object((1,3,6,1,4,1,629,231,3,1))
if mibBuilder.loadTexts:nbsPartProgTable.setStatus(_A)
_NbsPartProgEntry_Object=MibTableRow
nbsPartProgEntry=_NbsPartProgEntry_Object((1,3,6,1,4,1,629,231,3,1,1))
nbsPartProgEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:nbsPartProgEntry.setStatus(_A)
_NbsPartProgIfIndex_Type=InterfaceIndex
_NbsPartProgIfIndex_Object=MibTableColumn
nbsPartProgIfIndex=_NbsPartProgIfIndex_Object((1,3,6,1,4,1,629,231,3,1,1,1),_NbsPartProgIfIndex_Type())
nbsPartProgIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsPartProgIfIndex.setStatus(_A)
_NbsPartProgPartIndex_Type=NbsTcPartIndex
_NbsPartProgPartIndex_Object=MibTableColumn
nbsPartProgPartIndex=_NbsPartProgPartIndex_Object((1,3,6,1,4,1,629,231,3,1,1,2),_NbsPartProgPartIndex_Type())
nbsPartProgPartIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsPartProgPartIndex.setStatus(_A)
class _NbsPartProgFirmwareCaps_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_NbsPartProgFirmwareCaps_Type.__name__=_F
_NbsPartProgFirmwareCaps_Object=MibTableColumn
nbsPartProgFirmwareCaps=_NbsPartProgFirmwareCaps_Object((1,3,6,1,4,1,629,231,3,1,1,10),_NbsPartProgFirmwareCaps_Type())
nbsPartProgFirmwareCaps.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartProgFirmwareCaps.setStatus(_A)
class _NbsPartProgFirmwareLoad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_NbsPartProgFirmwareLoad_Type.__name__=_F
_NbsPartProgFirmwareLoad_Object=MibTableColumn
nbsPartProgFirmwareLoad=_NbsPartProgFirmwareLoad_Object((1,3,6,1,4,1,629,231,3,1,1,20),_NbsPartProgFirmwareLoad_Type())
nbsPartProgFirmwareLoad.setMaxAccess(_N)
if mibBuilder.loadTexts:nbsPartProgFirmwareLoad.setStatus(_A)
_NbsPartProgLoader_Type=Integer32
_NbsPartProgLoader_Object=MibTableColumn
nbsPartProgLoader=_NbsPartProgLoader_Object((1,3,6,1,4,1,629,231,3,1,1,21),_NbsPartProgLoader_Type())
nbsPartProgLoader.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartProgLoader.setStatus(_A)
_NbsPartProgNVAreaAdmin_Type=Integer32
_NbsPartProgNVAreaAdmin_Object=MibTableColumn
nbsPartProgNVAreaAdmin=_NbsPartProgNVAreaAdmin_Object((1,3,6,1,4,1,629,231,3,1,1,22),_NbsPartProgNVAreaAdmin_Type())
nbsPartProgNVAreaAdmin.setMaxAccess(_N)
if mibBuilder.loadTexts:nbsPartProgNVAreaAdmin.setStatus(_A)
class _NbsPartProgNVAreaOper_Type(Integer32):defaultValue=-1
_NbsPartProgNVAreaOper_Type.__name__=_G
_NbsPartProgNVAreaOper_Object=MibTableColumn
nbsPartProgNVAreaOper=_NbsPartProgNVAreaOper_Object((1,3,6,1,4,1,629,231,3,1,1,23),_NbsPartProgNVAreaOper_Type())
nbsPartProgNVAreaOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartProgNVAreaOper.setStatus(_A)
_NbsPartProgNVAreaStart_Type=Integer32
_NbsPartProgNVAreaStart_Object=MibTableColumn
nbsPartProgNVAreaStart=_NbsPartProgNVAreaStart_Object((1,3,6,1,4,1,629,231,3,1,1,30),_NbsPartProgNVAreaStart_Type())
nbsPartProgNVAreaStart.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartProgNVAreaStart.setStatus(_A)
_NbsPartProgNVAreaBanks_Type=Integer32
_NbsPartProgNVAreaBanks_Object=MibTableColumn
nbsPartProgNVAreaBanks=_NbsPartProgNVAreaBanks_Object((1,3,6,1,4,1,629,231,3,1,1,31),_NbsPartProgNVAreaBanks_Type())
nbsPartProgNVAreaBanks.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsPartProgNVAreaBanks.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nbsPartMib':nbsPartMib,'nbsPartHardGrp':nbsPartHardGrp,'nbsPartHardTable':nbsPartHardTable,'nbsPartHardEntry':nbsPartHardEntry,_H:nbsPartHardIfIndex,_I:nbsPartHardPartIndex,'nbsPartHardDescription':nbsPartHardDescription,'nbsPartHardSerialNumber':nbsPartHardSerialNumber,'nbsPartHardProductionId':nbsPartHardProductionId,'nbsPartHardVendor':nbsPartHardVendor,'nbsPartHardModel':nbsPartHardModel,'nbsPartHardWareRev':nbsPartHardWareRev,'nbsPartFirmGrp':nbsPartFirmGrp,'nbsPartFirmTable':nbsPartFirmTable,'nbsPartFirmEntry':nbsPartFirmEntry,_J:nbsPartFirmIfIndex,_K:nbsPartFirmPartIndex,'nbsPartFirmFpgaRev':nbsPartFirmFpgaRev,'nbsPartFirmSwMajor':nbsPartFirmSwMajor,'nbsPartFirmSwMinor':nbsPartFirmSwMinor,'nbsPartFirmSwBuild':nbsPartFirmSwBuild,'nbsPartFirmWareIndex':nbsPartFirmWareIndex,'nbsPartProgGrp':nbsPartProgGrp,'nbsPartProgTable':nbsPartProgTable,'nbsPartProgEntry':nbsPartProgEntry,_L:nbsPartProgIfIndex,_M:nbsPartProgPartIndex,'nbsPartProgFirmwareCaps':nbsPartProgFirmwareCaps,'nbsPartProgFirmwareLoad':nbsPartProgFirmwareLoad,'nbsPartProgLoader':nbsPartProgLoader,'nbsPartProgNVAreaAdmin':nbsPartProgNVAreaAdmin,'nbsPartProgNVAreaOper':nbsPartProgNVAreaOper,'nbsPartProgNVAreaStart':nbsPartProgNVAreaStart,'nbsPartProgNVAreaBanks':nbsPartProgNVAreaBanks})
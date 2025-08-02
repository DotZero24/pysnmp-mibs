_H='not-accessible'
_G='cdSerialNumIndex'
_F='cdMacAddrIndex'
_E='BRCM-CABLEDATA-FACTORY-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataPrivateMIBObjects,=mibBuilder.importSymbols('BRCM-CABLEDATA-PRIVATE-MIB','cableDataPrivateMIBObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
cableDataFactory=ModuleIdentity((1,3,6,1,4,1,4413,2,99,1,1,2))
if mibBuilder.loadTexts:cableDataFactory.setRevisions(('2011-05-12 00:00','2007-02-05 00:00','2002-06-19 00:00'))
_CableDataFactoryBase_ObjectIdentity=ObjectIdentity
cableDataFactoryBase=_CableDataFactoryBase_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,1))
_CdFactCommitSettings_Type=TruthValue
_CdFactCommitSettings_Object=MibScalar
cdFactCommitSettings=_CdFactCommitSettings_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,1),_CdFactCommitSettings_Type())
cdFactCommitSettings.setMaxAccess(_B)
if mibBuilder.loadTexts:cdFactCommitSettings.setStatus(_A)
_CdFactScratchPad_Type=Unsigned32
_CdFactScratchPad_Object=MibScalar
cdFactScratchPad=_CdFactScratchPad_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,2),_CdFactScratchPad_Type())
cdFactScratchPad.setMaxAccess(_B)
if mibBuilder.loadTexts:cdFactScratchPad.setStatus(_A)
_CdFactSerialNumberTable_Object=MibTable
cdFactSerialNumberTable=_CdFactSerialNumberTable_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,3))
if mibBuilder.loadTexts:cdFactSerialNumberTable.setStatus(_A)
_CdFactSerialNumberEntry_Object=MibTableRow
cdFactSerialNumberEntry=_CdFactSerialNumberEntry_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,3,1))
cdFactSerialNumberEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:cdFactSerialNumberEntry.setStatus(_A)
class _CdSerialNumIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CdSerialNumIndex_Type.__name__=_C
_CdSerialNumIndex_Object=MibTableColumn
cdSerialNumIndex=_CdSerialNumIndex_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,3,1,1),_CdSerialNumIndex_Type())
cdSerialNumIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cdSerialNumIndex.setStatus(_A)
_CdSerialNumber_Type=OctetString
_CdSerialNumber_Object=MibTableColumn
cdSerialNumber=_CdSerialNumber_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,3,1,2),_CdSerialNumber_Type())
cdSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cdSerialNumber.setStatus(_A)
_CdSerialNumDescr_Type=DisplayString
_CdSerialNumDescr_Object=MibTableColumn
cdSerialNumDescr=_CdSerialNumDescr_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,3,1,3),_CdSerialNumDescr_Type())
cdSerialNumDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:cdSerialNumDescr.setStatus(_A)
_CdFactMacAddressTable_Object=MibTable
cdFactMacAddressTable=_CdFactMacAddressTable_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,4))
if mibBuilder.loadTexts:cdFactMacAddressTable.setStatus(_A)
_CdFactMacAddressEntry_Object=MibTableRow
cdFactMacAddressEntry=_CdFactMacAddressEntry_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,4,1))
cdFactMacAddressEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cdFactMacAddressEntry.setStatus(_A)
class _CdMacAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CdMacAddrIndex_Type.__name__=_C
_CdMacAddrIndex_Object=MibTableColumn
cdMacAddrIndex=_CdMacAddrIndex_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,4,1,1),_CdMacAddrIndex_Type())
cdMacAddrIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cdMacAddrIndex.setStatus(_A)
_CdMacAddress_Type=MacAddress
_CdMacAddress_Object=MibTableColumn
cdMacAddress=_CdMacAddress_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,4,1,2),_CdMacAddress_Type())
cdMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cdMacAddress.setStatus(_A)
class _CdMacAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
_CdMacAddrType_Type.__name__=_C
_CdMacAddrType_Object=MibTableColumn
cdMacAddrType=_CdMacAddrType_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,4,1,3),_CdMacAddrType_Type())
cdMacAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cdMacAddrType.setStatus(_A)
_CdMacAddrDescr_Type=DisplayString
_CdMacAddrDescr_Object=MibTableColumn
cdMacAddrDescr=_CdMacAddrDescr_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,4,1,4),_CdMacAddrDescr_Type())
cdMacAddrDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:cdMacAddrDescr.setStatus(_A)
_CdFactIpSettingsTable_Object=MibTable
cdFactIpSettingsTable=_CdFactIpSettingsTable_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,5))
if mibBuilder.loadTexts:cdFactIpSettingsTable.setStatus(_A)
_CdFactIpSettingsEntry_Object=MibTableRow
cdFactIpSettingsEntry=_CdFactIpSettingsEntry_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,5,1))
cdFactIpSettingsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cdFactIpSettingsEntry.setStatus(_A)
_CdIpDescr_Type=DisplayString
_CdIpDescr_Object=MibTableColumn
cdIpDescr=_CdIpDescr_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,5,1,1),_CdIpDescr_Type())
cdIpDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:cdIpDescr.setStatus(_A)
class _CdIpProvMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('static',0),('dynamic',1)))
_CdIpProvMethod_Type.__name__=_C
_CdIpProvMethod_Object=MibTableColumn
cdIpProvMethod=_CdIpProvMethod_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,5,1,2),_CdIpProvMethod_Type())
cdIpProvMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:cdIpProvMethod.setStatus(_A)
_CdIpStaticAddress_Type=IpAddress
_CdIpStaticAddress_Object=MibTableColumn
cdIpStaticAddress=_CdIpStaticAddress_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,5,1,3),_CdIpStaticAddress_Type())
cdIpStaticAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cdIpStaticAddress.setStatus(_A)
_CdIpStaticSubnet_Type=IpAddress
_CdIpStaticSubnet_Object=MibTableColumn
cdIpStaticSubnet=_CdIpStaticSubnet_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,5,1,4),_CdIpStaticSubnet_Type())
cdIpStaticSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cdIpStaticSubnet.setStatus(_A)
_CdIpStaticGateway_Type=IpAddress
_CdIpStaticGateway_Object=MibTableColumn
cdIpStaticGateway=_CdIpStaticGateway_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,5,1,5),_CdIpStaticGateway_Type())
cdIpStaticGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:cdIpStaticGateway.setStatus(_A)
class _CdFactNonVolOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('idle',0),('readPending',1),('reading',2),('writePending',3),('writing',4)))
_CdFactNonVolOperStatus_Type.__name__=_C
_CdFactNonVolOperStatus_Object=MibScalar
cdFactNonVolOperStatus=_CdFactNonVolOperStatus_Object((1,3,6,1,4,1,4413,2,99,1,1,2,1,6),_CdFactNonVolOperStatus_Type())
cdFactNonVolOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cdFactNonVolOperStatus.setStatus(_A)
_CableDataFactoryVendor_ObjectIdentity=ObjectIdentity
cableDataFactoryVendor=_CableDataFactoryVendor_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,99))
mibBuilder.exportSymbols(_E,**{'cableDataFactory':cableDataFactory,'cableDataFactoryBase':cableDataFactoryBase,'cdFactCommitSettings':cdFactCommitSettings,'cdFactScratchPad':cdFactScratchPad,'cdFactSerialNumberTable':cdFactSerialNumberTable,'cdFactSerialNumberEntry':cdFactSerialNumberEntry,_G:cdSerialNumIndex,'cdSerialNumber':cdSerialNumber,'cdSerialNumDescr':cdSerialNumDescr,'cdFactMacAddressTable':cdFactMacAddressTable,'cdFactMacAddressEntry':cdFactMacAddressEntry,_F:cdMacAddrIndex,'cdMacAddress':cdMacAddress,'cdMacAddrType':cdMacAddrType,'cdMacAddrDescr':cdMacAddrDescr,'cdFactIpSettingsTable':cdFactIpSettingsTable,'cdFactIpSettingsEntry':cdFactIpSettingsEntry,'cdIpDescr':cdIpDescr,'cdIpProvMethod':cdIpProvMethod,'cdIpStaticAddress':cdIpStaticAddress,'cdIpStaticSubnet':cdIpStaticSubnet,'cdIpStaticGateway':cdIpStaticGateway,'cdFactNonVolOperStatus':cdFactNonVolOperStatus,'cableDataFactoryVendor':cableDataFactoryVendor})
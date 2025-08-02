_K='asrSrvcRegMIBGroup'
_J='asrSrvcRegRowStatus'
_I='asrSrvcRegParm1'
_H='asrSrvcRegATMAddress'
_G='asrSrvcRegAddressIndex'
_F='asrSrvcRegServiceID'
_E='asrSrvcRegPort'
_D='read-create'
_C='not-accessible'
_B='CISCO-ATM-SERVICE-REGISTRY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoAtmServiceRegistryMIB=ModuleIdentity((1,3,6,1,4,1,9,9,50))
if mibBuilder.loadTexts:ciscoAtmServiceRegistryMIB.setRevisions(('1996-02-04 00:00',))
class AtmAddr(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8),ValueSizeConstraint(13,13),ValueSizeConstraint(20,20))
class InterfaceIndexOrZero(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoAtmServiceRegistryMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAtmServiceRegistryMIBObjects=_CiscoAtmServiceRegistryMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,50,1))
_AsrSrvcRegTable_Object=MibTable
asrSrvcRegTable=_AsrSrvcRegTable_Object((1,3,6,1,4,1,9,9,50,1,1))
if mibBuilder.loadTexts:asrSrvcRegTable.setStatus(_A)
_AsrSrvcRegEntry_Object=MibTableRow
asrSrvcRegEntry=_AsrSrvcRegEntry_Object((1,3,6,1,4,1,9,9,50,1,1,1))
asrSrvcRegEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:asrSrvcRegEntry.setStatus(_A)
_AsrSrvcRegPort_Type=InterfaceIndexOrZero
_AsrSrvcRegPort_Object=MibTableColumn
asrSrvcRegPort=_AsrSrvcRegPort_Object((1,3,6,1,4,1,9,9,50,1,1,1,1),_AsrSrvcRegPort_Type())
asrSrvcRegPort.setMaxAccess(_C)
if mibBuilder.loadTexts:asrSrvcRegPort.setStatus(_A)
_AsrSrvcRegServiceID_Type=ObjectIdentifier
_AsrSrvcRegServiceID_Object=MibTableColumn
asrSrvcRegServiceID=_AsrSrvcRegServiceID_Object((1,3,6,1,4,1,9,9,50,1,1,1,2),_AsrSrvcRegServiceID_Type())
asrSrvcRegServiceID.setMaxAccess(_C)
if mibBuilder.loadTexts:asrSrvcRegServiceID.setStatus(_A)
_AsrSrvcRegATMAddress_Type=AtmAddr
_AsrSrvcRegATMAddress_Object=MibTableColumn
asrSrvcRegATMAddress=_AsrSrvcRegATMAddress_Object((1,3,6,1,4,1,9,9,50,1,1,1,3),_AsrSrvcRegATMAddress_Type())
asrSrvcRegATMAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:asrSrvcRegATMAddress.setStatus(_A)
_AsrSrvcRegAddressIndex_Type=Integer32
_AsrSrvcRegAddressIndex_Object=MibTableColumn
asrSrvcRegAddressIndex=_AsrSrvcRegAddressIndex_Object((1,3,6,1,4,1,9,9,50,1,1,1,4),_AsrSrvcRegAddressIndex_Type())
asrSrvcRegAddressIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:asrSrvcRegAddressIndex.setStatus(_A)
_AsrSrvcRegParm1_Type=OctetString
_AsrSrvcRegParm1_Object=MibTableColumn
asrSrvcRegParm1=_AsrSrvcRegParm1_Object((1,3,6,1,4,1,9,9,50,1,1,1,5),_AsrSrvcRegParm1_Type())
asrSrvcRegParm1.setMaxAccess(_D)
if mibBuilder.loadTexts:asrSrvcRegParm1.setStatus(_A)
_AsrSrvcRegRowStatus_Type=RowStatus
_AsrSrvcRegRowStatus_Object=MibTableColumn
asrSrvcRegRowStatus=_AsrSrvcRegRowStatus_Object((1,3,6,1,4,1,9,9,50,1,1,1,6),_AsrSrvcRegRowStatus_Type())
asrSrvcRegRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:asrSrvcRegRowStatus.setStatus(_A)
_AsrSrvcRegMIBConformance_ObjectIdentity=ObjectIdentity
asrSrvcRegMIBConformance=_AsrSrvcRegMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,50,3))
_AsrSrvcRegMIBCompliances_ObjectIdentity=ObjectIdentity
asrSrvcRegMIBCompliances=_AsrSrvcRegMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,50,3,1))
_AsrSrvcRegMIBGroups_ObjectIdentity=ObjectIdentity
asrSrvcRegMIBGroups=_AsrSrvcRegMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,50,3,2))
asrSrvcRegMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,50,3,2,1))
asrSrvcRegMIBGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:asrSrvcRegMIBGroup.setStatus(_A)
asrSrvcRegMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,50,3,1,1))
asrSrvcRegMIBCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:asrSrvcRegMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AtmAddr':AtmAddr,'InterfaceIndexOrZero':InterfaceIndexOrZero,'ciscoAtmServiceRegistryMIB':ciscoAtmServiceRegistryMIB,'ciscoAtmServiceRegistryMIBObjects':ciscoAtmServiceRegistryMIBObjects,'asrSrvcRegTable':asrSrvcRegTable,'asrSrvcRegEntry':asrSrvcRegEntry,_E:asrSrvcRegPort,_F:asrSrvcRegServiceID,_H:asrSrvcRegATMAddress,_G:asrSrvcRegAddressIndex,_I:asrSrvcRegParm1,_J:asrSrvcRegRowStatus,'asrSrvcRegMIBConformance':asrSrvcRegMIBConformance,'asrSrvcRegMIBCompliances':asrSrvcRegMIBCompliances,'asrSrvcRegMIBCompliance':asrSrvcRegMIBCompliance,'asrSrvcRegMIBGroups':asrSrvcRegMIBGroups,_K:asrSrvcRegMIBGroup})
_L='hpicfCoreDumpConfigGroup'
_K='hpicfCoreDumpTftpServerAddressType'
_J='hpicfCoreDumpTftpServerAddress'
_I='hpicfCoreDumpImStatus'
_H='hpicfCoreDumpMmStatus'
_G='disabled'
_F='enabled'
_E='hpicfCoreDumpModule'
_D='read-write'
_C='Integer32'
_B='HP-ICF-CORE-DUMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpicfCommon,=mibBuilder.importSymbols('HP-ICF-OID','hpicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfCoreDumpMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,1,14))
if mibBuilder.loadTexts:hpicfCoreDumpMIB.setRevisions(('2010-06-13 00:00',))
_HpicfCoreDumpObjects_ObjectIdentity=ObjectIdentity
hpicfCoreDumpObjects=_HpicfCoreDumpObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,14,1))
_HpicfCoreDumpConfig_ObjectIdentity=ObjectIdentity
hpicfCoreDumpConfig=_HpicfCoreDumpConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,14,1,1))
_HpicfCoreDumpTable_Object=MibTable
hpicfCoreDumpTable=_HpicfCoreDumpTable_Object((1,3,6,1,4,1,11,2,14,11,1,14,1,1,1))
if mibBuilder.loadTexts:hpicfCoreDumpTable.setStatus(_A)
_HpicfCoreDumpEntry_Object=MibTableRow
hpicfCoreDumpEntry=_HpicfCoreDumpEntry_Object((1,3,6,1,4,1,11,2,14,11,1,14,1,1,1,1))
hpicfCoreDumpEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hpicfCoreDumpEntry.setStatus(_A)
class _HpicfCoreDumpModule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfCoreDumpModule_Type.__name__=_C
_HpicfCoreDumpModule_Object=MibTableColumn
hpicfCoreDumpModule=_HpicfCoreDumpModule_Object((1,3,6,1,4,1,11,2,14,11,1,14,1,1,1,1,1),_HpicfCoreDumpModule_Type())
hpicfCoreDumpModule.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfCoreDumpModule.setStatus(_A)
class _HpicfCoreDumpMmStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpicfCoreDumpMmStatus_Type.__name__=_C
_HpicfCoreDumpMmStatus_Object=MibTableColumn
hpicfCoreDumpMmStatus=_HpicfCoreDumpMmStatus_Object((1,3,6,1,4,1,11,2,14,11,1,14,1,1,1,1,2),_HpicfCoreDumpMmStatus_Type())
hpicfCoreDumpMmStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfCoreDumpMmStatus.setStatus(_A)
class _HpicfCoreDumpImStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpicfCoreDumpImStatus_Type.__name__=_C
_HpicfCoreDumpImStatus_Object=MibTableColumn
hpicfCoreDumpImStatus=_HpicfCoreDumpImStatus_Object((1,3,6,1,4,1,11,2,14,11,1,14,1,1,1,1,3),_HpicfCoreDumpImStatus_Type())
hpicfCoreDumpImStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfCoreDumpImStatus.setStatus(_A)
_HpicfCoreDumpTftpServerAddressType_Type=InetAddressType
_HpicfCoreDumpTftpServerAddressType_Object=MibScalar
hpicfCoreDumpTftpServerAddressType=_HpicfCoreDumpTftpServerAddressType_Object((1,3,6,1,4,1,11,2,14,11,1,14,1,1,2),_HpicfCoreDumpTftpServerAddressType_Type())
hpicfCoreDumpTftpServerAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfCoreDumpTftpServerAddressType.setStatus(_A)
_HpicfCoreDumpTftpServerAddress_Type=InetAddress
_HpicfCoreDumpTftpServerAddress_Object=MibScalar
hpicfCoreDumpTftpServerAddress=_HpicfCoreDumpTftpServerAddress_Object((1,3,6,1,4,1,11,2,14,11,1,14,1,1,3),_HpicfCoreDumpTftpServerAddress_Type())
hpicfCoreDumpTftpServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfCoreDumpTftpServerAddress.setStatus(_A)
_HpicfCoreDumpConformance_ObjectIdentity=ObjectIdentity
hpicfCoreDumpConformance=_HpicfCoreDumpConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,14,2))
_HpicfCoreDumpConfigGroups_ObjectIdentity=ObjectIdentity
hpicfCoreDumpConfigGroups=_HpicfCoreDumpConfigGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,14,2,1))
_HpicfCoreDumpCompliances_ObjectIdentity=ObjectIdentity
hpicfCoreDumpCompliances=_HpicfCoreDumpCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,14,2,2))
hpicfCoreDumpConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,14,2,1,1))
hpicfCoreDumpConfigGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:hpicfCoreDumpConfigGroup.setStatus(_A)
hpicfCoreDumpCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,14,2,2,1))
hpicfCoreDumpCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:hpicfCoreDumpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfCoreDumpMIB':hpicfCoreDumpMIB,'hpicfCoreDumpObjects':hpicfCoreDumpObjects,'hpicfCoreDumpConfig':hpicfCoreDumpConfig,'hpicfCoreDumpTable':hpicfCoreDumpTable,'hpicfCoreDumpEntry':hpicfCoreDumpEntry,_E:hpicfCoreDumpModule,_H:hpicfCoreDumpMmStatus,_I:hpicfCoreDumpImStatus,_K:hpicfCoreDumpTftpServerAddressType,_J:hpicfCoreDumpTftpServerAddress,'hpicfCoreDumpConformance':hpicfCoreDumpConformance,'hpicfCoreDumpConfigGroups':hpicfCoreDumpConfigGroups,_L:hpicfCoreDumpConfigGroup,'hpicfCoreDumpCompliances':hpicfCoreDumpCompliances,'hpicfCoreDumpCompliance':hpicfCoreDumpCompliance})
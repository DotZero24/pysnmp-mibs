_O='rbnMplsL3VpnGroup'
_N='rbnMplsL3VpnVrfRTDescr'
_M='rbnMplsL3VpnVrfRT'
_L='read-only'
_K='rbnMplsL3VpnVrfRTIndex'
_J='rbnMplsL3VpnVrfRTType'
_I='rbnMplsL3VpnVrfRTAddrFamily'
_H='Unsigned32'
_G='SnmpAdminString'
_F='mplsL3VpnVrfName'
_E='MplsL3VpnRouteDistinguisher'
_D='MPLS-L3VPN-STD-MIB'
_C='not-accessible'
_B='RBN-MPLS-L3VPN-STD-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
MplsL3VpnRouteDistinguisher,MplsL3VpnRtType,mplsL3VpnVrfName=mibBuilder.importSymbols(_D,_E,'MplsL3VpnRtType',_F)
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnMplsL3VpnMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,51))
if mibBuilder.loadTexts:rbnMplsL3VpnMIB.setRevisions(('2009-05-30 00:00',))
_RbnMplsL3VpnObjects_ObjectIdentity=ObjectIdentity
rbnMplsL3VpnObjects=_RbnMplsL3VpnObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,51,1))
_RbnMplsL3VpnConf_ObjectIdentity=ObjectIdentity
rbnMplsL3VpnConf=_RbnMplsL3VpnConf_ObjectIdentity((1,3,6,1,4,1,2352,2,51,1,1))
_RbnMplsL3VpnVrfRTTable_Object=MibTable
rbnMplsL3VpnVrfRTTable=_RbnMplsL3VpnVrfRTTable_Object((1,3,6,1,4,1,2352,2,51,1,1,1))
if mibBuilder.loadTexts:rbnMplsL3VpnVrfRTTable.setStatus(_A)
_RbnMplsL3VpnVrfRTEntry_Object=MibTableRow
rbnMplsL3VpnVrfRTEntry=_RbnMplsL3VpnVrfRTEntry_Object((1,3,6,1,4,1,2352,2,51,1,1,1,1))
rbnMplsL3VpnVrfRTEntry.setIndexNames((0,_D,_F),(0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:rbnMplsL3VpnVrfRTEntry.setStatus(_A)
_RbnMplsL3VpnVrfRTAddrFamily_Type=AddressFamilyNumbers
_RbnMplsL3VpnVrfRTAddrFamily_Object=MibTableColumn
rbnMplsL3VpnVrfRTAddrFamily=_RbnMplsL3VpnVrfRTAddrFamily_Object((1,3,6,1,4,1,2352,2,51,1,1,1,1,1),_RbnMplsL3VpnVrfRTAddrFamily_Type())
rbnMplsL3VpnVrfRTAddrFamily.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMplsL3VpnVrfRTAddrFamily.setStatus(_A)
_RbnMplsL3VpnVrfRTType_Type=MplsL3VpnRtType
_RbnMplsL3VpnVrfRTType_Object=MibTableColumn
rbnMplsL3VpnVrfRTType=_RbnMplsL3VpnVrfRTType_Object((1,3,6,1,4,1,2352,2,51,1,1,1,1,2),_RbnMplsL3VpnVrfRTType_Type())
rbnMplsL3VpnVrfRTType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMplsL3VpnVrfRTType.setStatus(_A)
class _RbnMplsL3VpnVrfRTIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RbnMplsL3VpnVrfRTIndex_Type.__name__=_H
_RbnMplsL3VpnVrfRTIndex_Object=MibTableColumn
rbnMplsL3VpnVrfRTIndex=_RbnMplsL3VpnVrfRTIndex_Object((1,3,6,1,4,1,2352,2,51,1,1,1,1,3),_RbnMplsL3VpnVrfRTIndex_Type())
rbnMplsL3VpnVrfRTIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMplsL3VpnVrfRTIndex.setStatus(_A)
class _RbnMplsL3VpnVrfRT_Type(MplsL3VpnRouteDistinguisher):defaultValue=OctetString('')
_RbnMplsL3VpnVrfRT_Type.__name__=_E
_RbnMplsL3VpnVrfRT_Object=MibTableColumn
rbnMplsL3VpnVrfRT=_RbnMplsL3VpnVrfRT_Object((1,3,6,1,4,1,2352,2,51,1,1,1,1,4),_RbnMplsL3VpnVrfRT_Type())
rbnMplsL3VpnVrfRT.setMaxAccess(_L)
if mibBuilder.loadTexts:rbnMplsL3VpnVrfRT.setStatus(_A)
class _RbnMplsL3VpnVrfRTDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_RbnMplsL3VpnVrfRTDescr_Type.__name__=_G
_RbnMplsL3VpnVrfRTDescr_Object=MibTableColumn
rbnMplsL3VpnVrfRTDescr=_RbnMplsL3VpnVrfRTDescr_Object((1,3,6,1,4,1,2352,2,51,1,1,1,1,5),_RbnMplsL3VpnVrfRTDescr_Type())
rbnMplsL3VpnVrfRTDescr.setMaxAccess(_L)
if mibBuilder.loadTexts:rbnMplsL3VpnVrfRTDescr.setStatus(_A)
_RbnMplsL3VpnConformance_ObjectIdentity=ObjectIdentity
rbnMplsL3VpnConformance=_RbnMplsL3VpnConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,51,2))
_RbnMplsL3VpnGroups_ObjectIdentity=ObjectIdentity
rbnMplsL3VpnGroups=_RbnMplsL3VpnGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,51,2,1))
_RbnMplsL3VpnCompliances_ObjectIdentity=ObjectIdentity
rbnMplsL3VpnCompliances=_RbnMplsL3VpnCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,51,2,2))
rbnMplsL3VpnGroup=ObjectGroup((1,3,6,1,4,1,2352,2,51,2,1,1))
rbnMplsL3VpnGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:rbnMplsL3VpnGroup.setStatus(_A)
rbnMplsL3VpnModuleCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,51,2,2,1))
rbnMplsL3VpnModuleCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:rbnMplsL3VpnModuleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnMplsL3VpnMIB':rbnMplsL3VpnMIB,'rbnMplsL3VpnObjects':rbnMplsL3VpnObjects,'rbnMplsL3VpnConf':rbnMplsL3VpnConf,'rbnMplsL3VpnVrfRTTable':rbnMplsL3VpnVrfRTTable,'rbnMplsL3VpnVrfRTEntry':rbnMplsL3VpnVrfRTEntry,_I:rbnMplsL3VpnVrfRTAddrFamily,_J:rbnMplsL3VpnVrfRTType,_K:rbnMplsL3VpnVrfRTIndex,_M:rbnMplsL3VpnVrfRT,_N:rbnMplsL3VpnVrfRTDescr,'rbnMplsL3VpnConformance':rbnMplsL3VpnConformance,'rbnMplsL3VpnGroups':rbnMplsL3VpnGroups,_O:rbnMplsL3VpnGroup,'rbnMplsL3VpnCompliances':rbnMplsL3VpnCompliances,'rbnMplsL3VpnModuleCompliance':rbnMplsL3VpnModuleCompliance})
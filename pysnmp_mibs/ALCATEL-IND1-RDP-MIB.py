_V='alaRDPConfigMIBGroup'
_U='alaRDPVrrpStatus'
_T='alaRDPIPIfStatus'
_S='alaRDPIfName'
_R='alaRDPIfRowStatus'
_Q='alaRDPIfPrefLevel'
_P='alaRDPIfAdvLifeTime'
_O='alaRDPIfMinAdvtInterval'
_N='alaRDPIfMaxAdvtInterval'
_M='alaRDPIfAdvtAddress'
_L='alaRDPIfStatus'
_K='alaRDPStatus'
_J='RowStatus'
_I='Unsigned32'
_H='alaRDPIfAddr'
_G='disabled'
_F='enabled'
_E='read-only'
_D='read-create'
_C='Integer32'
_B='ALCATEL-IND1-RDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1RDP,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','routingIND1RDP')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_J,'TextualConvention')
alcatelIND1RouterDiscoveryProtocolMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,11,1))
if mibBuilder.loadTexts:alcatelIND1RouterDiscoveryProtocolMIB.setRevisions(('2007-04-03 00:00',))
_AlcatelIND1RDPMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1RDPMIBObjects=_AlcatelIND1RDPMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1))
_AlaRDPConfig_ObjectIdentity=ObjectIdentity
alaRDPConfig=_AlaRDPConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1))
class _AlaRDPStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaRDPStatus_Type.__name__=_C
_AlaRDPStatus_Object=MibScalar
alaRDPStatus=_AlaRDPStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,1),_AlaRDPStatus_Type())
alaRDPStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:alaRDPStatus.setStatus(_A)
_AlaRDPIfTable_Object=MibTable
alaRDPIfTable=_AlaRDPIfTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,20))
if mibBuilder.loadTexts:alaRDPIfTable.setStatus(_A)
_AlaRDPIfEntry_Object=MibTableRow
alaRDPIfEntry=_AlaRDPIfEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,20,1))
alaRDPIfEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:alaRDPIfEntry.setStatus(_A)
_AlaRDPIfAddr_Type=IpAddress
_AlaRDPIfAddr_Object=MibTableColumn
alaRDPIfAddr=_AlaRDPIfAddr_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,20,1,1),_AlaRDPIfAddr_Type())
alaRDPIfAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRDPIfAddr.setStatus(_A)
class _AlaRDPIfStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaRDPIfStatus_Type.__name__=_C
_AlaRDPIfStatus_Object=MibTableColumn
alaRDPIfStatus=_AlaRDPIfStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,20,1,2),_AlaRDPIfStatus_Type())
alaRDPIfStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRDPIfStatus.setStatus(_A)
_AlaRDPIfAdvtAddress_Type=IpAddress
_AlaRDPIfAdvtAddress_Object=MibTableColumn
alaRDPIfAdvtAddress=_AlaRDPIfAdvtAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,20,1,3),_AlaRDPIfAdvtAddress_Type())
alaRDPIfAdvtAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRDPIfAdvtAddress.setStatus(_A)
class _AlaRDPIfMaxAdvtInterval_Type(Unsigned32):defaultValue=600
_AlaRDPIfMaxAdvtInterval_Type.__name__=_I
_AlaRDPIfMaxAdvtInterval_Object=MibTableColumn
alaRDPIfMaxAdvtInterval=_AlaRDPIfMaxAdvtInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,20,1,4),_AlaRDPIfMaxAdvtInterval_Type())
alaRDPIfMaxAdvtInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRDPIfMaxAdvtInterval.setStatus(_A)
_AlaRDPIfMinAdvtInterval_Type=Unsigned32
_AlaRDPIfMinAdvtInterval_Object=MibTableColumn
alaRDPIfMinAdvtInterval=_AlaRDPIfMinAdvtInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,20,1,5),_AlaRDPIfMinAdvtInterval_Type())
alaRDPIfMinAdvtInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRDPIfMinAdvtInterval.setStatus(_A)
_AlaRDPIfAdvLifeTime_Type=Unsigned32
_AlaRDPIfAdvLifeTime_Object=MibTableColumn
alaRDPIfAdvLifeTime=_AlaRDPIfAdvLifeTime_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,20,1,6),_AlaRDPIfAdvLifeTime_Type())
alaRDPIfAdvLifeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRDPIfAdvLifeTime.setStatus(_A)
class _AlaRDPIfPrefLevel_Type(Integer32):defaultValue=0
_AlaRDPIfPrefLevel_Type.__name__=_C
_AlaRDPIfPrefLevel_Object=MibTableColumn
alaRDPIfPrefLevel=_AlaRDPIfPrefLevel_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,20,1,7),_AlaRDPIfPrefLevel_Type())
alaRDPIfPrefLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRDPIfPrefLevel.setStatus(_A)
class _AlaRDPIfRowStatus_Type(RowStatus):defaultValue=2
_AlaRDPIfRowStatus_Type.__name__=_J
_AlaRDPIfRowStatus_Object=MibTableColumn
alaRDPIfRowStatus=_AlaRDPIfRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,20,1,8),_AlaRDPIfRowStatus_Type())
alaRDPIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRDPIfRowStatus.setStatus(_A)
_AlaRDPIfName_Type=DisplayString
_AlaRDPIfName_Object=MibTableColumn
alaRDPIfName=_AlaRDPIfName_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,20,1,9),_AlaRDPIfName_Type())
alaRDPIfName.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRDPIfName.setStatus(_A)
class _AlaRDPIPIfStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaRDPIPIfStatus_Type.__name__=_C
_AlaRDPIPIfStatus_Object=MibTableColumn
alaRDPIPIfStatus=_AlaRDPIPIfStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,20,1,10),_AlaRDPIPIfStatus_Type())
alaRDPIPIfStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRDPIPIfStatus.setStatus(_A)
class _AlaRDPVrrpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaRDPVrrpStatus_Type.__name__=_C
_AlaRDPVrrpStatus_Object=MibTableColumn
alaRDPVrrpStatus=_AlaRDPVrrpStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,1,1,20,1,11),_AlaRDPVrrpStatus_Type())
alaRDPVrrpStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRDPVrrpStatus.setStatus(_A)
_AlcatelIND1RDPMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1RDPMIBConformance=_AlcatelIND1RDPMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,2))
_AlcatelIND1RDPMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1RDPMIBCompliances=_AlcatelIND1RDPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,2,1))
_AlcatelIND1RDPMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1RDPMIBGroups=_AlcatelIND1RDPMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,2,2))
alaRDPConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,2,2,1))
alaRDPConfigMIBGroup.setObjects(*((_B,_K),(_B,_H),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:alaRDPConfigMIBGroup.setStatus(_A)
alcatelIND1RDPMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,11,1,2,1,1))
alcatelIND1RDPMIBCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:alcatelIND1RDPMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1RouterDiscoveryProtocolMIB':alcatelIND1RouterDiscoveryProtocolMIB,'alcatelIND1RDPMIBObjects':alcatelIND1RDPMIBObjects,'alaRDPConfig':alaRDPConfig,_K:alaRDPStatus,'alaRDPIfTable':alaRDPIfTable,'alaRDPIfEntry':alaRDPIfEntry,_H:alaRDPIfAddr,_L:alaRDPIfStatus,_M:alaRDPIfAdvtAddress,_N:alaRDPIfMaxAdvtInterval,_O:alaRDPIfMinAdvtInterval,_P:alaRDPIfAdvLifeTime,_Q:alaRDPIfPrefLevel,_R:alaRDPIfRowStatus,_S:alaRDPIfName,_T:alaRDPIPIfStatus,_U:alaRDPVrrpStatus,'alcatelIND1RDPMIBConformance':alcatelIND1RDPMIBConformance,'alcatelIND1RDPMIBCompliances':alcatelIND1RDPMIBCompliances,'alcatelIND1RDPMIBCompliance':alcatelIND1RDPMIBCompliance,'alcatelIND1RDPMIBGroups':alcatelIND1RDPMIBGroups,_V:alaRDPConfigMIBGroup})
_X='t38FaxRelayGroupRev1'
_W='t38FaxRelayGroup'
_V='t38Redundancy'
_U='t38ErrCorrection'
_T='t38FaxInfoFieldSize'
_S='t38vismDs1Number'
_R='t38T30ECM'
_Q='t38FxLCO'
_P='t38NseAckTimeOut'
_O='t38NSFVendorCode'
_N='t38NSFCountryCode'
_M='t38NSFOverride'
_L='t38TCFmethod'
_K='t38HsDataRedundancy'
_J='t38LsDataRedundancy'
_I='t38HsDataPacketSize'
_H='t38MaxFaxTxRate'
_G='disabled'
_F='enabled'
_E='deprecated'
_D='read-write'
_C='current'
_B='Integer32'
_A='CISCO-WAN-T38-FAXRELAY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanT38FaxRelayMIB=ModuleIdentity((1,3,6,1,4,1,351,150,19))
if mibBuilder.loadTexts:ciscoWanT38FaxRelayMIB.setRevisions(('2004-02-19 00:00','2002-06-01 00:00','2002-04-12 15:00'))
_CiscoWanT38FaxRelayMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWanT38FaxRelayMIBObjects=_CiscoWanT38FaxRelayMIBObjects_ObjectIdentity((1,3,6,1,4,1,351,150,19,1))
_T38FaxRelayGrp_ObjectIdentity=ObjectIdentity
t38FaxRelayGrp=_T38FaxRelayGrp_ObjectIdentity((1,3,6,1,4,1,351,150,19,1,1))
_T38FaxRelayGrpTable_Object=MibTable
t38FaxRelayGrpTable=_T38FaxRelayGrpTable_Object((1,3,6,1,4,1,351,150,19,1,1,1))
if mibBuilder.loadTexts:t38FaxRelayGrpTable.setStatus(_C)
_T38FaxRelayGrpEntry_Object=MibTableRow
t38FaxRelayGrpEntry=_T38FaxRelayGrpEntry_Object((1,3,6,1,4,1,351,150,19,1,1,1,1))
t38FaxRelayGrpEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:t38FaxRelayGrpEntry.setStatus(_C)
class _T38vismDs1Number_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_T38vismDs1Number_Type.__name__=_B
_T38vismDs1Number_Object=MibTableColumn
t38vismDs1Number=_T38vismDs1Number_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,1),_T38vismDs1Number_Type())
t38vismDs1Number.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:t38vismDs1Number.setStatus(_C)
class _T38MaxFaxTxRate_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('fx2400bps',1),('fx4800bps',2),('fx7200bps',3),('fx9600bps',4),('fx12000bps',5),('fx14400bps',6)))
_T38MaxFaxTxRate_Type.__name__=_B
_T38MaxFaxTxRate_Object=MibTableColumn
t38MaxFaxTxRate=_T38MaxFaxTxRate_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,2),_T38MaxFaxTxRate_Type())
t38MaxFaxTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:t38MaxFaxTxRate.setStatus(_C)
class _T38FaxInfoFieldSize_Type(Integer32):defaultValue=48;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_T38FaxInfoFieldSize_Type.__name__=_B
_T38FaxInfoFieldSize_Object=MibTableColumn
t38FaxInfoFieldSize=_T38FaxInfoFieldSize_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,3),_T38FaxInfoFieldSize_Type())
t38FaxInfoFieldSize.setMaxAccess(_D)
if mibBuilder.loadTexts:t38FaxInfoFieldSize.setStatus(_E)
class _T38HsDataPacketSize_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,20,30,40)));namedValues=NamedValues(*(('tenms',10),('twentyms',20),('thirtyms',30),('fortyms',40)))
_T38HsDataPacketSize_Type.__name__=_B
_T38HsDataPacketSize_Object=MibTableColumn
t38HsDataPacketSize=_T38HsDataPacketSize_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,4),_T38HsDataPacketSize_Type())
t38HsDataPacketSize.setMaxAccess(_D)
if mibBuilder.loadTexts:t38HsDataPacketSize.setStatus(_C)
class _T38LsDataRedundancy_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_T38LsDataRedundancy_Type.__name__=_B
_T38LsDataRedundancy_Object=MibTableColumn
t38LsDataRedundancy=_T38LsDataRedundancy_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,5),_T38LsDataRedundancy_Type())
t38LsDataRedundancy.setMaxAccess(_D)
if mibBuilder.loadTexts:t38LsDataRedundancy.setStatus(_C)
class _T38HsDataRedundancy_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_T38HsDataRedundancy_Type.__name__=_B
_T38HsDataRedundancy_Object=MibTableColumn
t38HsDataRedundancy=_T38HsDataRedundancy_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,6),_T38HsDataRedundancy_Type())
t38HsDataRedundancy.setMaxAccess(_D)
if mibBuilder.loadTexts:t38HsDataRedundancy.setStatus(_C)
class _T38TCFmethod_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('localTCF',1),('networkTCF',2)))
_T38TCFmethod_Type.__name__=_B
_T38TCFmethod_Object=MibTableColumn
t38TCFmethod=_T38TCFmethod_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,7),_T38TCFmethod_Type())
t38TCFmethod.setMaxAccess(_D)
if mibBuilder.loadTexts:t38TCFmethod.setStatus(_C)
class _T38ErrCorrection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_T38ErrCorrection_Type.__name__=_B
_T38ErrCorrection_Object=MibTableColumn
t38ErrCorrection=_T38ErrCorrection_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,8),_T38ErrCorrection_Type())
t38ErrCorrection.setMaxAccess(_D)
if mibBuilder.loadTexts:t38ErrCorrection.setStatus(_E)
class _T38NSFOverride_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_T38NSFOverride_Type.__name__=_B
_T38NSFOverride_Object=MibTableColumn
t38NSFOverride=_T38NSFOverride_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,9),_T38NSFOverride_Type())
t38NSFOverride.setMaxAccess(_D)
if mibBuilder.loadTexts:t38NSFOverride.setStatus(_C)
class _T38NSFCountryCode_Type(Integer32):defaultValue=173;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_T38NSFCountryCode_Type.__name__=_B
_T38NSFCountryCode_Object=MibTableColumn
t38NSFCountryCode=_T38NSFCountryCode_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,10),_T38NSFCountryCode_Type())
t38NSFCountryCode.setMaxAccess(_D)
if mibBuilder.loadTexts:t38NSFCountryCode.setStatus(_C)
class _T38NSFVendorCode_Type(Integer32):defaultValue=81;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_T38NSFVendorCode_Type.__name__=_B
_T38NSFVendorCode_Object=MibTableColumn
t38NSFVendorCode=_T38NSFVendorCode_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,11),_T38NSFVendorCode_Type())
t38NSFVendorCode.setMaxAccess(_D)
if mibBuilder.loadTexts:t38NSFVendorCode.setStatus(_C)
class _T38NseAckTimeOut_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(250,10000))
_T38NseAckTimeOut_Type.__name__=_B
_T38NseAckTimeOut_Object=MibTableColumn
t38NseAckTimeOut=_T38NseAckTimeOut_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,12),_T38NseAckTimeOut_Type())
t38NseAckTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:t38NseAckTimeOut.setStatus(_C)
if mibBuilder.loadTexts:t38NseAckTimeOut.setUnits('milliseconds')
class _T38FxLCO_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('gwAndPt',1),('gw',2),('ptAndGw',3),('pt',4),('off',5)))
_T38FxLCO_Type.__name__=_B
_T38FxLCO_Object=MibTableColumn
t38FxLCO=_T38FxLCO_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,13),_T38FxLCO_Type())
t38FxLCO.setMaxAccess(_D)
if mibBuilder.loadTexts:t38FxLCO.setStatus(_C)
class _T38Redundancy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_T38Redundancy_Type.__name__=_B
_T38Redundancy_Object=MibTableColumn
t38Redundancy=_T38Redundancy_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,14),_T38Redundancy_Type())
t38Redundancy.setMaxAccess(_D)
if mibBuilder.loadTexts:t38Redundancy.setStatus(_E)
class _T38T30ECM_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_T38T30ECM_Type.__name__=_B
_T38T30ECM_Object=MibTableColumn
t38T30ECM=_T38T30ECM_Object((1,3,6,1,4,1,351,150,19,1,1,1,1,15),_T38T30ECM_Type())
t38T30ECM.setMaxAccess(_D)
if mibBuilder.loadTexts:t38T30ECM.setStatus(_C)
_T38NotificationPrefix_ObjectIdentity=ObjectIdentity
t38NotificationPrefix=_T38NotificationPrefix_ObjectIdentity((1,3,6,1,4,1,351,150,19,2))
_T38Notifications_ObjectIdentity=ObjectIdentity
t38Notifications=_T38Notifications_ObjectIdentity((1,3,6,1,4,1,351,150,19,2,0))
_T38FaxRelayMIBConformance_ObjectIdentity=ObjectIdentity
t38FaxRelayMIBConformance=_T38FaxRelayMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,19,3))
_T38FaxRelayMIBCompliances_ObjectIdentity=ObjectIdentity
t38FaxRelayMIBCompliances=_T38FaxRelayMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,19,3,1))
_T38FaxRelayMIBGroups_ObjectIdentity=ObjectIdentity
t38FaxRelayMIBGroups=_T38FaxRelayMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,19,3,2))
t38FaxRelayGroup=ObjectGroup((1,3,6,1,4,1,351,150,19,3,2,1))
t38FaxRelayGroup.setObjects(*((_A,_H),(_A,_T),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_U),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_V),(_A,_R)))
if mibBuilder.loadTexts:t38FaxRelayGroup.setStatus(_E)
t38FaxRelayGroupRev1=ObjectGroup((1,3,6,1,4,1,351,150,19,3,2,2))
t38FaxRelayGroupRev1.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:t38FaxRelayGroupRev1.setStatus(_C)
t38FaxRelayMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,19,3,1,1))
t38FaxRelayMIBCompliance.setObjects((_A,_W))
if mibBuilder.loadTexts:t38FaxRelayMIBCompliance.setStatus(_E)
t38FaxRelayMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,351,150,19,3,1,2))
t38FaxRelayMIBComplianceRev1.setObjects((_A,_X))
if mibBuilder.loadTexts:t38FaxRelayMIBComplianceRev1.setStatus(_C)
mibBuilder.exportSymbols(_A,**{'ciscoWanT38FaxRelayMIB':ciscoWanT38FaxRelayMIB,'ciscoWanT38FaxRelayMIBObjects':ciscoWanT38FaxRelayMIBObjects,'t38FaxRelayGrp':t38FaxRelayGrp,'t38FaxRelayGrpTable':t38FaxRelayGrpTable,'t38FaxRelayGrpEntry':t38FaxRelayGrpEntry,_S:t38vismDs1Number,_H:t38MaxFaxTxRate,_T:t38FaxInfoFieldSize,_I:t38HsDataPacketSize,_J:t38LsDataRedundancy,_K:t38HsDataRedundancy,_L:t38TCFmethod,_U:t38ErrCorrection,_M:t38NSFOverride,_N:t38NSFCountryCode,_O:t38NSFVendorCode,_P:t38NseAckTimeOut,_Q:t38FxLCO,_V:t38Redundancy,_R:t38T30ECM,'t38NotificationPrefix':t38NotificationPrefix,'t38Notifications':t38Notifications,'t38FaxRelayMIBConformance':t38FaxRelayMIBConformance,'t38FaxRelayMIBCompliances':t38FaxRelayMIBCompliances,'t38FaxRelayMIBCompliance':t38FaxRelayMIBCompliance,'t38FaxRelayMIBComplianceRev1':t38FaxRelayMIBComplianceRev1,'t38FaxRelayMIBGroups':t38FaxRelayMIBGroups,_W:t38FaxRelayGroup,_X:t38FaxRelayGroupRev1})
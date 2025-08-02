_N='alvarionBandwidthControlLevelMIBGroup'
_M='alvarionBandwidthControlMIBGroup'
_L='coBandwidthControlLevelMaxReceiveRate'
_K='coBandwidthControlLevelMinReceiveRate'
_J='coBandwidthControlLevelMaxTransmitRate'
_I='coBandwidthControlLevelMinTransmitRate'
_H='coBandwidthControlMaxReceiveRate'
_G='coBandwidthControlMaxTransmitRate'
_F='coBandwidthControlEnable'
_E='coBandwidthControlLevelIndex'
_D='Integer32'
_C='read-only'
_B='ALVARION-BANDWIDTH-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
AlvarionPriorityQueue,=mibBuilder.importSymbols('ALVARION-TC','AlvarionPriorityQueue')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
alvarionBandwidthControlMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,14))
_AlvarionBandwidthControlMIBObjects_ObjectIdentity=ObjectIdentity
alvarionBandwidthControlMIBObjects=_AlvarionBandwidthControlMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,14,1))
_CoBandwidthControlConfig_ObjectIdentity=ObjectIdentity
coBandwidthControlConfig=_CoBandwidthControlConfig_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,14,1,1))
_CoBandwidthControlEnable_Type=TruthValue
_CoBandwidthControlEnable_Object=MibScalar
coBandwidthControlEnable=_CoBandwidthControlEnable_Object((1,3,6,1,4,1,12394,1,10,5,14,1,1,1),_CoBandwidthControlEnable_Type())
coBandwidthControlEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:coBandwidthControlEnable.setStatus(_A)
_CoBandwidthControlMaxTransmitRate_Type=Integer32
_CoBandwidthControlMaxTransmitRate_Object=MibScalar
coBandwidthControlMaxTransmitRate=_CoBandwidthControlMaxTransmitRate_Object((1,3,6,1,4,1,12394,1,10,5,14,1,1,2),_CoBandwidthControlMaxTransmitRate_Type())
coBandwidthControlMaxTransmitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coBandwidthControlMaxTransmitRate.setStatus(_A)
_CoBandwidthControlMaxReceiveRate_Type=Integer32
_CoBandwidthControlMaxReceiveRate_Object=MibScalar
coBandwidthControlMaxReceiveRate=_CoBandwidthControlMaxReceiveRate_Object((1,3,6,1,4,1,12394,1,10,5,14,1,1,3),_CoBandwidthControlMaxReceiveRate_Type())
coBandwidthControlMaxReceiveRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coBandwidthControlMaxReceiveRate.setStatus(_A)
_CoBandwidthControlLevelTable_Object=MibTable
coBandwidthControlLevelTable=_CoBandwidthControlLevelTable_Object((1,3,6,1,4,1,12394,1,10,5,14,1,1,4))
if mibBuilder.loadTexts:coBandwidthControlLevelTable.setStatus(_A)
_CoBandwidthControlLevelEntry_Object=MibTableRow
coBandwidthControlLevelEntry=_CoBandwidthControlLevelEntry_Object((1,3,6,1,4,1,12394,1,10,5,14,1,1,4,1))
coBandwidthControlLevelEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:coBandwidthControlLevelEntry.setStatus(_A)
_CoBandwidthControlLevelIndex_Type=AlvarionPriorityQueue
_CoBandwidthControlLevelIndex_Object=MibTableColumn
coBandwidthControlLevelIndex=_CoBandwidthControlLevelIndex_Object((1,3,6,1,4,1,12394,1,10,5,14,1,1,4,1,1),_CoBandwidthControlLevelIndex_Type())
coBandwidthControlLevelIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:coBandwidthControlLevelIndex.setStatus(_A)
class _CoBandwidthControlLevelMinTransmitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CoBandwidthControlLevelMinTransmitRate_Type.__name__=_D
_CoBandwidthControlLevelMinTransmitRate_Object=MibTableColumn
coBandwidthControlLevelMinTransmitRate=_CoBandwidthControlLevelMinTransmitRate_Object((1,3,6,1,4,1,12394,1,10,5,14,1,1,4,1,2),_CoBandwidthControlLevelMinTransmitRate_Type())
coBandwidthControlLevelMinTransmitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coBandwidthControlLevelMinTransmitRate.setStatus(_A)
class _CoBandwidthControlLevelMaxTransmitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CoBandwidthControlLevelMaxTransmitRate_Type.__name__=_D
_CoBandwidthControlLevelMaxTransmitRate_Object=MibTableColumn
coBandwidthControlLevelMaxTransmitRate=_CoBandwidthControlLevelMaxTransmitRate_Object((1,3,6,1,4,1,12394,1,10,5,14,1,1,4,1,3),_CoBandwidthControlLevelMaxTransmitRate_Type())
coBandwidthControlLevelMaxTransmitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coBandwidthControlLevelMaxTransmitRate.setStatus(_A)
class _CoBandwidthControlLevelMinReceiveRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CoBandwidthControlLevelMinReceiveRate_Type.__name__=_D
_CoBandwidthControlLevelMinReceiveRate_Object=MibTableColumn
coBandwidthControlLevelMinReceiveRate=_CoBandwidthControlLevelMinReceiveRate_Object((1,3,6,1,4,1,12394,1,10,5,14,1,1,4,1,4),_CoBandwidthControlLevelMinReceiveRate_Type())
coBandwidthControlLevelMinReceiveRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coBandwidthControlLevelMinReceiveRate.setStatus(_A)
class _CoBandwidthControlLevelMaxReceiveRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CoBandwidthControlLevelMaxReceiveRate_Type.__name__=_D
_CoBandwidthControlLevelMaxReceiveRate_Object=MibTableColumn
coBandwidthControlLevelMaxReceiveRate=_CoBandwidthControlLevelMaxReceiveRate_Object((1,3,6,1,4,1,12394,1,10,5,14,1,1,4,1,5),_CoBandwidthControlLevelMaxReceiveRate_Type())
coBandwidthControlLevelMaxReceiveRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coBandwidthControlLevelMaxReceiveRate.setStatus(_A)
_AlvarionBandwidthControlMIBConformance_ObjectIdentity=ObjectIdentity
alvarionBandwidthControlMIBConformance=_AlvarionBandwidthControlMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,14,2))
_AlvarionBandwidthControlMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionBandwidthControlMIBCompliances=_AlvarionBandwidthControlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,14,2,1))
_AlvarionBandwidthControlMIBGroups_ObjectIdentity=ObjectIdentity
alvarionBandwidthControlMIBGroups=_AlvarionBandwidthControlMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,14,2,2))
alvarionBandwidthControlMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,14,2,2,1))
alvarionBandwidthControlMIBGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:alvarionBandwidthControlMIBGroup.setStatus(_A)
alvarionBandwidthControlLevelMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,14,2,2,2))
alvarionBandwidthControlLevelMIBGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:alvarionBandwidthControlLevelMIBGroup.setStatus(_A)
alvarionBandwidthControlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,14,2,1,1))
alvarionBandwidthControlMIBCompliance.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:alvarionBandwidthControlMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alvarionBandwidthControlMIB':alvarionBandwidthControlMIB,'alvarionBandwidthControlMIBObjects':alvarionBandwidthControlMIBObjects,'coBandwidthControlConfig':coBandwidthControlConfig,_F:coBandwidthControlEnable,_G:coBandwidthControlMaxTransmitRate,_H:coBandwidthControlMaxReceiveRate,'coBandwidthControlLevelTable':coBandwidthControlLevelTable,'coBandwidthControlLevelEntry':coBandwidthControlLevelEntry,_E:coBandwidthControlLevelIndex,_I:coBandwidthControlLevelMinTransmitRate,_J:coBandwidthControlLevelMaxTransmitRate,_K:coBandwidthControlLevelMinReceiveRate,_L:coBandwidthControlLevelMaxReceiveRate,'alvarionBandwidthControlMIBConformance':alvarionBandwidthControlMIBConformance,'alvarionBandwidthControlMIBCompliances':alvarionBandwidthControlMIBCompliances,'alvarionBandwidthControlMIBCompliance':alvarionBandwidthControlMIBCompliance,'alvarionBandwidthControlMIBGroups':alvarionBandwidthControlMIBGroups,_M:alvarionBandwidthControlMIBGroup,_N:alvarionBandwidthControlLevelMIBGroup})
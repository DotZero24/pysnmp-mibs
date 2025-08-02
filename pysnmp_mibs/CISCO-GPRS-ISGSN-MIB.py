_K='cgprsIsgsnStatsGroup'
_J='cgprsIsgsnErrorCountRxToTnode'
_I='cgprsIsgsnErrorCountRxFromTnode'
_H='cgprsIsgsnTxOctetCountToTnode'
_G='cgprsIsgsnRxOctetCountFromTnode'
_F='cgprsIsgsnTxPacketCountToTnode'
_E='cgprsIsgsnRxPacketCountFromTnode'
_D='packets'
_C='read-only'
_B='CISCO-GPRS-ISGSN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoGprsIsgsnMIB=ModuleIdentity((1,3,6,1,4,1,9,9,9992))
_CiscoGprsIsgsnMIBObjects_ObjectIdentity=ObjectIdentity
ciscoGprsIsgsnMIBObjects=_CiscoGprsIsgsnMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,9992,1))
_CiscoGprsIsgsnStats_ObjectIdentity=ObjectIdentity
ciscoGprsIsgsnStats=_CiscoGprsIsgsnStats_ObjectIdentity((1,3,6,1,4,1,9,9,9992,1,1))
_CgprsIsgsnRxPacketCountFromTnode_Type=Counter32
_CgprsIsgsnRxPacketCountFromTnode_Object=MibScalar
cgprsIsgsnRxPacketCountFromTnode=_CgprsIsgsnRxPacketCountFromTnode_Object((1,3,6,1,4,1,9,9,9992,1,1,1),_CgprsIsgsnRxPacketCountFromTnode_Type())
cgprsIsgsnRxPacketCountFromTnode.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsIsgsnRxPacketCountFromTnode.setStatus(_A)
if mibBuilder.loadTexts:cgprsIsgsnRxPacketCountFromTnode.setUnits(_D)
_CgprsIsgsnTxPacketCountToTnode_Type=Counter32
_CgprsIsgsnTxPacketCountToTnode_Object=MibScalar
cgprsIsgsnTxPacketCountToTnode=_CgprsIsgsnTxPacketCountToTnode_Object((1,3,6,1,4,1,9,9,9992,1,1,2),_CgprsIsgsnTxPacketCountToTnode_Type())
cgprsIsgsnTxPacketCountToTnode.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsIsgsnTxPacketCountToTnode.setStatus(_A)
if mibBuilder.loadTexts:cgprsIsgsnTxPacketCountToTnode.setUnits(_D)
_CgprsIsgsnRxOctetCountFromTnode_Type=Counter32
_CgprsIsgsnRxOctetCountFromTnode_Object=MibScalar
cgprsIsgsnRxOctetCountFromTnode=_CgprsIsgsnRxOctetCountFromTnode_Object((1,3,6,1,4,1,9,9,9992,1,1,3),_CgprsIsgsnRxOctetCountFromTnode_Type())
cgprsIsgsnRxOctetCountFromTnode.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsIsgsnRxOctetCountFromTnode.setStatus(_A)
if mibBuilder.loadTexts:cgprsIsgsnRxOctetCountFromTnode.setUnits('bytes')
_CgprsIsgsnTxOctetCountToTnode_Type=Counter32
_CgprsIsgsnTxOctetCountToTnode_Object=MibScalar
cgprsIsgsnTxOctetCountToTnode=_CgprsIsgsnTxOctetCountToTnode_Object((1,3,6,1,4,1,9,9,9992,1,1,4),_CgprsIsgsnTxOctetCountToTnode_Type())
cgprsIsgsnTxOctetCountToTnode.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsIsgsnTxOctetCountToTnode.setStatus(_A)
if mibBuilder.loadTexts:cgprsIsgsnTxOctetCountToTnode.setUnits('bytes')
_CgprsIsgsnErrorCountRxFromTnode_Type=Counter32
_CgprsIsgsnErrorCountRxFromTnode_Object=MibScalar
cgprsIsgsnErrorCountRxFromTnode=_CgprsIsgsnErrorCountRxFromTnode_Object((1,3,6,1,4,1,9,9,9992,1,1,5),_CgprsIsgsnErrorCountRxFromTnode_Type())
cgprsIsgsnErrorCountRxFromTnode.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsIsgsnErrorCountRxFromTnode.setStatus(_A)
if mibBuilder.loadTexts:cgprsIsgsnErrorCountRxFromTnode.setUnits(_D)
_CgprsIsgsnErrorCountRxToTnode_Type=Counter32
_CgprsIsgsnErrorCountRxToTnode_Object=MibScalar
cgprsIsgsnErrorCountRxToTnode=_CgprsIsgsnErrorCountRxToTnode_Object((1,3,6,1,4,1,9,9,9992,1,1,6),_CgprsIsgsnErrorCountRxToTnode_Type())
cgprsIsgsnErrorCountRxToTnode.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsIsgsnErrorCountRxToTnode.setStatus(_A)
if mibBuilder.loadTexts:cgprsIsgsnErrorCountRxToTnode.setUnits(_D)
_CiscoGprsIsgsnConformances_ObjectIdentity=ObjectIdentity
ciscoGprsIsgsnConformances=_CiscoGprsIsgsnConformances_ObjectIdentity((1,3,6,1,4,1,9,9,9992,3))
_CgprsIsgsnGroups_ObjectIdentity=ObjectIdentity
cgprsIsgsnGroups=_CgprsIsgsnGroups_ObjectIdentity((1,3,6,1,4,1,9,9,9992,3,1))
_CgprsIsgsnCompliances_ObjectIdentity=ObjectIdentity
cgprsIsgsnCompliances=_CgprsIsgsnCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,9992,3,2))
cgprsIsgsnStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,9992,3,1,1))
cgprsIsgsnStatsGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cgprsIsgsnStatsGroup.setStatus(_A)
cgprsIsgsnCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,9992,3,2,1))
cgprsIsgsnCompliance1.setObjects((_B,_K))
if mibBuilder.loadTexts:cgprsIsgsnCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoGprsIsgsnMIB':ciscoGprsIsgsnMIB,'ciscoGprsIsgsnMIBObjects':ciscoGprsIsgsnMIBObjects,'ciscoGprsIsgsnStats':ciscoGprsIsgsnStats,_E:cgprsIsgsnRxPacketCountFromTnode,_F:cgprsIsgsnTxPacketCountToTnode,_G:cgprsIsgsnRxOctetCountFromTnode,_H:cgprsIsgsnTxOctetCountToTnode,_I:cgprsIsgsnErrorCountRxFromTnode,_J:cgprsIsgsnErrorCountRxToTnode,'ciscoGprsIsgsnConformances':ciscoGprsIsgsnConformances,'cgprsIsgsnGroups':cgprsIsgsnGroups,_K:cgprsIsgsnStatsGroup,'cgprsIsgsnCompliances':cgprsIsgsnCompliances,'cgprsIsgsnCompliance1':cgprsIsgsnCompliance1})
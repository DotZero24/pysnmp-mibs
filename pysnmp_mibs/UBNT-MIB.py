_H='ubntORInfoGroup'
_G='ubntORDescr'
_F='ubntORID'
_E='read-only'
_D='ubntORIndex'
_C='Integer32'
_B='UBNT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ubntMIB=ModuleIdentity((1,3,6,1,4,1,41112,1))
if mibBuilder.loadTexts:ubntMIB.setRevisions(('2019-11-29 00:00',))
_Ubnt_ObjectIdentity=ObjectIdentity
ubnt=_Ubnt_ObjectIdentity((1,3,6,1,4,1,41112))
_UbntORTable_Object=MibTable
ubntORTable=_UbntORTable_Object((1,3,6,1,4,1,41112,1,1))
if mibBuilder.loadTexts:ubntORTable.setStatus(_A)
_UbntOREntry_Object=MibTableRow
ubntOREntry=_UbntOREntry_Object((1,3,6,1,4,1,41112,1,1,1))
ubntOREntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:ubntOREntry.setStatus(_A)
class _UbntORIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_UbntORIndex_Type.__name__=_C
_UbntORIndex_Object=MibTableColumn
ubntORIndex=_UbntORIndex_Object((1,3,6,1,4,1,41112,1,1,1,1),_UbntORIndex_Type())
ubntORIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ubntORIndex.setStatus(_A)
_UbntORID_Type=ObjectIdentifier
_UbntORID_Object=MibTableColumn
ubntORID=_UbntORID_Object((1,3,6,1,4,1,41112,1,1,1,2),_UbntORID_Type())
ubntORID.setMaxAccess(_E)
if mibBuilder.loadTexts:ubntORID.setStatus(_A)
_UbntORDescr_Type=DisplayString
_UbntORDescr_Object=MibTableColumn
ubntORDescr=_UbntORDescr_Object((1,3,6,1,4,1,41112,1,1,1,3),_UbntORDescr_Type())
ubntORDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:ubntORDescr.setStatus(_A)
_UbntSnmpInfo_ObjectIdentity=ObjectIdentity
ubntSnmpInfo=_UbntSnmpInfo_ObjectIdentity((1,3,6,1,4,1,41112,1,2))
_UbntSnmpGroups_ObjectIdentity=ObjectIdentity
ubntSnmpGroups=_UbntSnmpGroups_ObjectIdentity((1,3,6,1,4,1,41112,1,2,1))
_UbntAirosGroups_ObjectIdentity=ObjectIdentity
ubntAirosGroups=_UbntAirosGroups_ObjectIdentity((1,3,6,1,4,1,41112,1,2,2))
_UbntAirFiberGroups_ObjectIdentity=ObjectIdentity
ubntAirFiberGroups=_UbntAirFiberGroups_ObjectIdentity((1,3,6,1,4,1,41112,1,2,3))
_UbntEdgeMaxGroups_ObjectIdentity=ObjectIdentity
ubntEdgeMaxGroups=_UbntEdgeMaxGroups_ObjectIdentity((1,3,6,1,4,1,41112,1,2,4))
_UbntUniFiGroups_ObjectIdentity=ObjectIdentity
ubntUniFiGroups=_UbntUniFiGroups_ObjectIdentity((1,3,6,1,4,1,41112,1,2,5))
_UbntAirVisionGroups_ObjectIdentity=ObjectIdentity
ubntAirVisionGroups=_UbntAirVisionGroups_ObjectIdentity((1,3,6,1,4,1,41112,1,2,6))
_UbntMFiGroups_ObjectIdentity=ObjectIdentity
ubntMFiGroups=_UbntMFiGroups_ObjectIdentity((1,3,6,1,4,1,41112,1,2,7))
_UbntUniTelGroups_ObjectIdentity=ObjectIdentity
ubntUniTelGroups=_UbntUniTelGroups_ObjectIdentity((1,3,6,1,4,1,41112,1,2,8))
_UbntAFLTUGroups_ObjectIdentity=ObjectIdentity
ubntAFLTUGroups=_UbntAFLTUGroups_ObjectIdentity((1,3,6,1,4,1,41112,1,2,9))
_UbntSunMaxGroups_ObjectIdentity=ObjectIdentity
ubntSunMaxGroups=_UbntSunMaxGroups_ObjectIdentity((1,3,6,1,4,1,41112,1,2,10))
_UbntAirFIBER_ObjectIdentity=ObjectIdentity
ubntAirFIBER=_UbntAirFIBER_ObjectIdentity((1,3,6,1,4,1,41112,1,3))
_UbntAirMAX_ObjectIdentity=ObjectIdentity
ubntAirMAX=_UbntAirMAX_ObjectIdentity((1,3,6,1,4,1,41112,1,4))
_UbntEdgeMax_ObjectIdentity=ObjectIdentity
ubntEdgeMax=_UbntEdgeMax_ObjectIdentity((1,3,6,1,4,1,41112,1,5))
_UbntUniFi_ObjectIdentity=ObjectIdentity
ubntUniFi=_UbntUniFi_ObjectIdentity((1,3,6,1,4,1,41112,1,6))
_UbntAirVision_ObjectIdentity=ObjectIdentity
ubntAirVision=_UbntAirVision_ObjectIdentity((1,3,6,1,4,1,41112,1,7))
_UbntMFi_ObjectIdentity=ObjectIdentity
ubntMFi=_UbntMFi_ObjectIdentity((1,3,6,1,4,1,41112,1,8))
_UbntUniTel_ObjectIdentity=ObjectIdentity
ubntUniTel=_UbntUniTel_ObjectIdentity((1,3,6,1,4,1,41112,1,9))
_UbntAFLTU_ObjectIdentity=ObjectIdentity
ubntAFLTU=_UbntAFLTU_ObjectIdentity((1,3,6,1,4,1,41112,1,10))
_UbntSunMax_ObjectIdentity=ObjectIdentity
ubntSunMax=_UbntSunMax_ObjectIdentity((1,3,6,1,4,1,41112,1,11))
ubntORInfoGroup=ObjectGroup((1,3,6,1,4,1,41112,1,2,1,1))
ubntORInfoGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:ubntORInfoGroup.setStatus(_A)
ubntORCompliance=ModuleCompliance((1,3,6,1,4,1,41112,1,2,1,2))
ubntORCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:ubntORCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ubnt':ubnt,'ubntMIB':ubntMIB,'ubntORTable':ubntORTable,'ubntOREntry':ubntOREntry,_D:ubntORIndex,_F:ubntORID,_G:ubntORDescr,'ubntSnmpInfo':ubntSnmpInfo,'ubntSnmpGroups':ubntSnmpGroups,_H:ubntORInfoGroup,'ubntORCompliance':ubntORCompliance,'ubntAirosGroups':ubntAirosGroups,'ubntAirFiberGroups':ubntAirFiberGroups,'ubntEdgeMaxGroups':ubntEdgeMaxGroups,'ubntUniFiGroups':ubntUniFiGroups,'ubntAirVisionGroups':ubntAirVisionGroups,'ubntMFiGroups':ubntMFiGroups,'ubntUniTelGroups':ubntUniTelGroups,'ubntAFLTUGroups':ubntAFLTUGroups,'ubntSunMaxGroups':ubntSunMaxGroups,'ubntAirFIBER':ubntAirFIBER,'ubntAirMAX':ubntAirMAX,'ubntEdgeMax':ubntEdgeMax,'ubntUniFi':ubntUniFi,'ubntAirVision':ubntAirVision,'ubntMFi':ubntMFi,'ubntUniTel':ubntUniTel,'ubntAFLTU':ubntAFLTU,'ubntSunMax':ubntSunMax})
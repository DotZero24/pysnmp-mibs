_G='cyISPortNumber'
_F='CYCLADES-ACS-INFO-MIB'
_E='up'
_D='down'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cyACSMgmt,=mibBuilder.importSymbols('CYCLADES-ACS-MIB','cyACSMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cyACSInfo=ModuleIdentity((1,3,6,1,4,1,2925,4,3))
if mibBuilder.loadTexts:cyACSInfo.setRevisions(('2005-08-29 00:00','2002-09-20 00:00'))
_CyInfoSerialTable_Object=MibTable
cyInfoSerialTable=_CyInfoSerialTable_Object((1,3,6,1,4,1,2925,4,3,1))
if mibBuilder.loadTexts:cyInfoSerialTable.setStatus(_A)
_CyisPortEntry_Object=MibTableRow
cyisPortEntry=_CyisPortEntry_Object((1,3,6,1,4,1,2925,4,3,1,1))
cyisPortEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cyisPortEntry.setStatus(_A)
_CyISPortNumber_Type=InterfaceIndex
_CyISPortNumber_Object=MibTableColumn
cyISPortNumber=_CyISPortNumber_Object((1,3,6,1,4,1,2925,4,3,1,1,1),_CyISPortNumber_Type())
cyISPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortNumber.setStatus(_A)
_CyISPortTty_Type=DisplayString
_CyISPortTty_Object=MibTableColumn
cyISPortTty=_CyISPortTty_Object((1,3,6,1,4,1,2925,4,3,1,1,2),_CyISPortTty_Type())
cyISPortTty.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortTty.setStatus(_A)
_CyISPortName_Type=DisplayString
_CyISPortName_Object=MibTableColumn
cyISPortName=_CyISPortName_Object((1,3,6,1,4,1,2925,4,3,1,1,3),_CyISPortName_Type())
cyISPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortName.setStatus(_A)
_CyISPortSpeed_Type=Integer32
_CyISPortSpeed_Object=MibTableColumn
cyISPortSpeed=_CyISPortSpeed_Object((1,3,6,1,4,1,2925,4,3,1,1,4),_CyISPortSpeed_Type())
cyISPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortSpeed.setStatus(_A)
_CyISPortTxBytes_Type=Counter32
_CyISPortTxBytes_Object=MibTableColumn
cyISPortTxBytes=_CyISPortTxBytes_Object((1,3,6,1,4,1,2925,4,3,1,1,5),_CyISPortTxBytes_Type())
cyISPortTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortTxBytes.setStatus(_A)
_CyISPortRXBytes_Type=Counter32
_CyISPortRXBytes_Object=MibTableColumn
cyISPortRXBytes=_CyISPortRXBytes_Object((1,3,6,1,4,1,2925,4,3,1,1,6),_CyISPortRXBytes_Type())
cyISPortRXBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortRXBytes.setStatus(_A)
_CyISPortErrFrame_Type=Counter32
_CyISPortErrFrame_Object=MibTableColumn
cyISPortErrFrame=_CyISPortErrFrame_Object((1,3,6,1,4,1,2925,4,3,1,1,7),_CyISPortErrFrame_Type())
cyISPortErrFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortErrFrame.setStatus(_A)
_CyISPortErrParity_Type=Counter32
_CyISPortErrParity_Object=MibTableColumn
cyISPortErrParity=_CyISPortErrParity_Object((1,3,6,1,4,1,2925,4,3,1,1,8),_CyISPortErrParity_Type())
cyISPortErrParity.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortErrParity.setStatus(_A)
_CyISPortErrBreaks_Type=Counter32
_CyISPortErrBreaks_Object=MibTableColumn
cyISPortErrBreaks=_CyISPortErrBreaks_Object((1,3,6,1,4,1,2925,4,3,1,1,9),_CyISPortErrBreaks_Type())
cyISPortErrBreaks.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortErrBreaks.setStatus(_A)
_CyISPortErrOverrun_Type=Counter32
_CyISPortErrOverrun_Object=MibTableColumn
cyISPortErrOverrun=_CyISPortErrOverrun_Object((1,3,6,1,4,1,2925,4,3,1,1,10),_CyISPortErrOverrun_Type())
cyISPortErrOverrun.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortErrOverrun.setStatus(_A)
class _CyISPortSigDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CyISPortSigDTR_Type.__name__=_C
_CyISPortSigDTR_Object=MibTableColumn
cyISPortSigDTR=_CyISPortSigDTR_Object((1,3,6,1,4,1,2925,4,3,1,1,11),_CyISPortSigDTR_Type())
cyISPortSigDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortSigDTR.setStatus(_A)
class _CyISPortSigCD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CyISPortSigCD_Type.__name__=_C
_CyISPortSigCD_Object=MibTableColumn
cyISPortSigCD=_CyISPortSigCD_Object((1,3,6,1,4,1,2925,4,3,1,1,12),_CyISPortSigCD_Type())
cyISPortSigCD.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortSigCD.setStatus(_A)
class _CyISPortSigDSR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CyISPortSigDSR_Type.__name__=_C
_CyISPortSigDSR_Object=MibTableColumn
cyISPortSigDSR=_CyISPortSigDSR_Object((1,3,6,1,4,1,2925,4,3,1,1,13),_CyISPortSigDSR_Type())
cyISPortSigDSR.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortSigDSR.setStatus(_A)
class _CyISPortSigRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CyISPortSigRTS_Type.__name__=_C
_CyISPortSigRTS_Object=MibTableColumn
cyISPortSigRTS=_CyISPortSigRTS_Object((1,3,6,1,4,1,2925,4,3,1,1,14),_CyISPortSigRTS_Type())
cyISPortSigRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortSigRTS.setStatus(_A)
class _CyISPortSigCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CyISPortSigCTS_Type.__name__=_C
_CyISPortSigCTS_Object=MibTableColumn
cyISPortSigCTS=_CyISPortSigCTS_Object((1,3,6,1,4,1,2925,4,3,1,1,15),_CyISPortSigCTS_Type())
cyISPortSigCTS.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortSigCTS.setStatus(_A)
class _CyISPortSigRI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_CyISPortSigRI_Type.__name__=_C
_CyISPortSigRI_Object=MibTableColumn
cyISPortSigRI=_CyISPortSigRI_Object((1,3,6,1,4,1,2925,4,3,1,1,16),_CyISPortSigRI_Type())
cyISPortSigRI.setMaxAccess(_B)
if mibBuilder.loadTexts:cyISPortSigRI.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'cyACSInfo':cyACSInfo,'cyInfoSerialTable':cyInfoSerialTable,'cyisPortEntry':cyisPortEntry,_G:cyISPortNumber,'cyISPortTty':cyISPortTty,'cyISPortName':cyISPortName,'cyISPortSpeed':cyISPortSpeed,'cyISPortTxBytes':cyISPortTxBytes,'cyISPortRXBytes':cyISPortRXBytes,'cyISPortErrFrame':cyISPortErrFrame,'cyISPortErrParity':cyISPortErrParity,'cyISPortErrBreaks':cyISPortErrBreaks,'cyISPortErrOverrun':cyISPortErrOverrun,'cyISPortSigDTR':cyISPortSigDTR,'cyISPortSigCD':cyISPortSigCD,'cyISPortSigDSR':cyISPortSigDSR,'cyISPortSigRTS':cyISPortSigRTS,'cyISPortSigCTS':cyISPortSigCTS,'cyISPortSigRI':cyISPortSigRI})